import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import count
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType


aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.environ.get("AWS_SESSION_TOKEN")


# Create a SparkSession
spark = SparkSession.builder \
    .appName("Week6Lab") \
    .config("spark.sql.shuffle.partitions", "3") \
    .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider') \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.access.key", aws_access_key_id) \
    .config("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key) \
    .config("spark.hadoop.fs.s3a.session.token", aws_session_token) \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3,org.apache.hadoop:hadoop-aws:3.2.0,com.amazonaws:aws-java-sdk-bundle:1.11.375') \
    .master('local[*]') \
    .getOrCreate()

#For Windows users, quiet errors about not being able to delete temporary directories which make your logs impossible to read...
logger = spark.sparkContext._jvm.org.apache.log4j
logger.LogManager.getLogger("org.apache.spark.util.ShutdownHookManager"). setLevel( logger.Level.OFF )
logger.LogManager.getLogger("org.apache.spark.SparkEnv"). setLevel( logger.Level.ERROR )

silver_schema = StructType([
StructField("marketplace", StringType(), nullable=True)
,StructField("customer_id", StringType(), nullable=True)
,StructField("review_id", StringType(), nullable=True)
,StructField("product_id", StringType(), nullable=True)
,StructField("product_parent", StringType(), nullable=True)
,StructField("product_title", StringType(), nullable=True)
,StructField("product_category", StringType(), nullable=True)
,StructField("star_rating", IntegerType(), nullable=True)
,StructField("helpful_votes", IntegerType(), nullable=True)
,StructField("total_votes", IntegerType(), nullable=True)
,StructField("vine", StringType(), nullable=True)
,StructField("verified_purchase", StringType(), nullable=True)
,StructField("review_headline", StringType(), nullable=True)
,StructField("review_body", StringType(), nullable=True)
,StructField("purchase_date", StringType(), nullable=True)
,StructField("review_timestamp", TimestampType(), nullable=True)
,StructField("customer_name", StringType(), nullable=True)
,StructField("gender", StringType(), nullable=True)
,StructField("date_of_birth", StringType(), nullable=True)
,StructField("city", StringType(), nullable=True)
,StructField("state", StringType(), nullable=True)
])


silver_data = spark.readStream \
    .format("parquet") \
    .schema(silver_schema) \
    .load("s3a://hwe-tsagona/silver/reviews")
silver_data.createOrReplaceTempView("silver_reviews")

watermarked_data = silver_data \
    .withWatermark("review_timestamp", "10 seconds") 

# Perform the aggregation based on gender, state, star_rating, purchase_date, and product_title
aggregated_data = watermarked_data \
    .groupBy("gender", "state", "star_rating", "review_timestamp", "product_title") \
    .agg(count("*").alias("total"))

write_gold_query = aggregated_data \
    .writeStream \
    .format("parquet") \
.option("outputMode", "append") \
.option("path", "s3a://hwe-tsagona/gold/fact_review") \
.option("checkpointLocation", "/tmp/gold-checkpoint")

write_gold_query.start().awaitTermination()

## Stop the SparkSession
spark.stop()