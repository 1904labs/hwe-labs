import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
from pyspark.sql.functions import current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType

# Load environment variables.
from dotenv import load_dotenv
load_dotenv()

aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")


# Create a SparkSession
spark = SparkSession.builder \
    .appName("Week5Lab") \
    .config("spark.sql.shuffle.partitions", "3") \
    .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider') \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.access.key", aws_access_key_id) \
    .config("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key) \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3,org.apache.hadoop:hadoop-aws:3.2.0,com.amazonaws:aws-java-sdk-bundle:1.11.375') \
    .master('local[*]') \
    .getOrCreate()

#For Windows users, quiet errors about not being able to delete temporary directories which make your logs impossible to read...
logger = spark.sparkContext._jvm.org.apache.log4j
logger.LogManager.getLogger("org.apache.spark.util.ShutdownHookManager"). setLevel( logger.Level.OFF )
logger.LogManager.getLogger("org.apache.spark.SparkEnv"). setLevel( logger.Level.ERROR )

bronze_schema = StructType([
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
])

bronze_reviews = spark.readStream \
    .format("parquet") \
    .schema(bronze_schema) \
    .load("s3a://hwe-spring-2025/tsagona/bronze/reviews")
bronze_reviews.createOrReplaceTempView("bronze_reviews")

bronze_customers = spark.read.format("parquet").load("s3a://hwe-spring-2025/tsagona/bronze/customers")
bronze_customers.createOrReplaceTempView("bronze_customers")

silver_data = spark.sql("""
   select r.marketplace
         ,r.customer_id
         ,r.review_id
         ,r.product_id
         ,r.product_parent
         ,r.product_title
         ,r.product_category
         ,r.star_rating
         ,r.helpful_votes
         ,r.total_votes
         ,r.vine
         ,r.verified_purchase
         ,r.review_headline
         ,r.review_body
         ,r.purchase_date
         ,r.review_timestamp
         ,c.customer_name
         ,c.gender
         ,c.date_of_birth
         ,c.city
         ,c.state
    from bronze_reviews r
          inner join bronze_customers c
          on r.customer_id = c.customer_id
          where r.verified_purchase = 'Y'
    """)

streaming_query = silver_data.writeStream \
    .format("parquet") \
    .option("path", "s3a://hwe-spring-2025/tsagona/silver/reviews/") \
    .option("outputMode", "append") \
    .option("checkpointLocation", "/tmp/silver-checkpoint")

streaming_query.start().awaitTermination()

## Stop the SparkSession
spark.stop()
