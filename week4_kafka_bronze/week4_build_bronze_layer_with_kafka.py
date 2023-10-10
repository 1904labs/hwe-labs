import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Load environment variables.
from dotenv import load_dotenv
load_dotenv()

def getScramAuthString(username, password):
    return f"""org.apache.kafka.common.security.scram.ScramLoginModule required
   username="{username}"
   password="{password}";
  """


# Define the Kafka broker and topic to read from
kafka_bootstrap_servers = os.environ.get("HWE_BOOTSTRAP")
username = os.environ.get("HWE_USERNAME")
password = os.environ.get("HWE_PASSWORD")
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
kafka_topic = "reviews"

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Week4Lab") \
    .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider') \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.access.key", aws_access_key_id) \
    .config("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key) \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3,org.apache.hadoop:hadoop-aws:3.2.0,com.amazonaws:aws-java-sdk-bundle:1.11.375') \
    .config("spark.sql.shuffle.partitions", "3") \
    .getOrCreate()

# For Windows users, quiet errors about not being able to delete temporary directories which make your logs impossible to read...
logger = spark.sparkContext._jvm.org.apache.log4j
logger.LogManager.getLogger(
    "org.apache.spark.util.ShutdownHookManager"). setLevel(logger.Level.OFF)
logger.LogManager.getLogger(
    "org.apache.spark.SparkEnv"). setLevel(logger.Level.ERROR)

# Read data from Kafka using the DataFrame API
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", "earliest") \
    .option("maxOffsetsPerTrigger", "1000") \
    .option("kafka.security.protocol", "SASL_SSL") \
    .option("kafka.sasl.mechanism", "SCRAM-SHA-512") \
    .option("kafka.sasl.jaas.config", getScramAuthString(username, password)) \
    .load()

# Process the received data
query = df\
    .withColumn('marketplace', split(df['value'], '\t').getItem(0))\
    .withColumn('customer_id', split(df['value'], '\t').getItem(1))\
    .withColumn('review_id', split(df['value'], '\t').getItem(2))\
    .withColumn('product_id', split(df['value'], '\t').getItem(3))\
    .withColumn('product_parent', split(df['value'], '\t').getItem(4))\
    .withColumn('product_title', split(df['value'], '\t').getItem(5))\
    .withColumn('product_category', split(df['value'], '\t').getItem(6))\
    .withColumn('star_rating', split(df['value'], '\t').getItem(7))\
    .withColumn('helpful_vote', split(df['value'], '\t').getItem(8))\
    .withColumn('total_votes', split(df['value'], '\t').getItem(9))\
    .withColumn('vine', split(df['value'], '\t').getItem(10))\
    .withColumn('verified_purchase', split(df['value'], '\t').getItem(11))\
    .withColumn('review_headline', split(df['value'], '\t').getItem(12))\
    .withColumn('review_timestamp', current_timestamp())\
    .writeStream\
    .outputMode("append")\
    .format("parquet")\
    .option("path",
            "s3a://hwe-fall-2023/tseserman/bronze/reviews", )\
    .option("checkpointLocation", "/tmp/kafka-checkpoint")\
    .start()

# Wait for the streaming query to finish
query.awaitTermination()

# Stop the SparkSession
spark.stop()

# .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)",
# "CURRENT_TIMESTAMP() AS review_timestamp")\

#  .selectExpr("topic AS Topic",
#               "partition  as Partition",
#               "offset AS Offset",
#               "key AS Key",
#               "value as Value",
#               "CURRENT_TIMESTAMP() AS review_timestamp")\

#  .selectExpr(
#         "CAST(marketplace AS STRING)",
#         "CAST(customer_id AS INTEGER)",
#         "CAST(review_id AS STRING)",
#         "CAST(product_id AS STRING)",
#         "CAST(product_parent AS INTEGER)",
#         "CAST(product_title AS STRING)",
#         "CAST(product_category AS STRING)",
#         "CAST(star_rating AS INTEGER)",
#         "CAST(helpful_vote AS INTEGER)",
#         "CAST(total_votes AS INTEGER)",
#         "CAST(vine AS STRING)",
#         "CAST(verified_purchase AS STRING)",
#         "CAST(review_headline AS STRING)",
#         "CAST(review_body AS STRING)",
#         "CURRENT_TIMESTAMP()",
#     )

#  .selectExpr(
#         "CAST(value.marketplace AS STRING)",
#         "CAST(value.customer_id AS INTEGER)",
#         "CAST(value.review_id AS STRING)",
#         "CAST(value.product_id AS STRING)",
#         "CAST(value.product_parent AS INTEGER)",
#         "CAST(value.product_title AS STRING)",
#         "CAST(value.product_category AS STRING)",
#         "CAST(value.star_rating AS INTEGER)",
#         "CAST(value.helpful_vote AS INTEGER)",
#         "CAST(value.total_votes AS INTEGER)",
#         "CAST(value.vine AS STRING)",
#         "CAST(value.verified_purchase AS STRING)",
#         "CAST(value.review_headline AS STRING)",
#         "CAST(value.review_body AS STRING)",
#         "CURRENT_TIMESTAMP() as review_timestamp",
#     )
