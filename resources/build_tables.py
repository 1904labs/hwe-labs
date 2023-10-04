import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
from pyspark.sql.functions import current_timestamp

# Load environment variables.
from dotenv import load_dotenv
load_dotenv()


aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.environ.get("AWS_SESSION_TOKEN")


# Create a SparkSession
spark = SparkSession.builder \
    .appName("Week3Lab") \
    .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider') \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.access.key", aws_access_key_id) \
    .config("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key) \
    .config("spark.hadoop.fs.s3a.session.token", aws_session_token) \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3,org.apache.hadoop:hadoop-aws:3.2.0,com.amazonaws:aws-java-sdk-bundle:1.11.375') \
    .master('local[*]') \
    .getOrCreate()
    
spark.sql("CREATE DATABASE IF NOT EXISTS bronze")
spark.sql("DROP TABLE IF EXISTS bronze.reviews")
spark.sql("""
CREATE EXTERNAL TABLE bronze.reviews (
marketplace string,
customer_id string,
review_id string,
product_id string,
product_parent string,
product_title string,
product_category string,
star_rating string,
helpful_votes string,
total_votes string,
vine string,
verified_purchase string,
review_headline string,
review_body string,
purchase_date string,
review_timestamp timestamp)
STORED AS PARQUET
LOCATION
  's3a://hwe-tsagona/bronze/reviews'
""")

spark.sql("CREATE DATABASE IF NOT EXISTS silver")
spark.sql("DROP TABLE IF EXISTS silver.reviews")
spark.sql("""
CREATE EXTERNAL TABLE silver.reviews (
          marketplace string
         ,customer_id string
         ,review_id string
         ,product_id string
         ,product_parent string
         ,product_title string
         ,product_category string
         ,star_rating string
         ,helpful_votes string
         ,total_votes string
         ,vine string
         ,verified_purchase string
         ,review_headline string
         ,review_body string
         ,purchase_date string
         ,review_timestamp timestamp
         ,customer_name string
         ,gender string
         ,date_of_birth string
         ,city string
         ,state string)
STORED AS PARQUET
LOCATION
  's3a://hwe-tsagona/silver/reviews'
""")



#Create a table on top of the shared customers directory matching the schema from the file.
#Name this table bronze.customers
spark.sql("CREATE DATABASE IF NOT EXISTS bronze")
spark.sql("DROP TABLE IF EXISTS bronze.customers")
spark.sql("""
CREATE EXTERNAL TABLE bronze.customers (
     customer_id string
    ,customer_name string
    ,gender string
    ,date_of_birth string
    ,city string
    ,state string)
STORED AS PARQUET
LOCATION
  's3a://hwe-tsagona/bronze/customers'
""")

spark.sql("SHOW CREATE TABLE silver.reviews")

## Stop the SparkSession
spark.stop()
