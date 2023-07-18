import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
from pyspark.sql.functions import current_timestamp


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
    .config("spark.sql.catalogImplementation", "hive") \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3,org.apache.hadoop:hadoop-aws:3.2.0,com.amazonaws:aws-java-sdk-bundle:1.11.375') \
    .enableHiveSupport()\
    .getOrCreate()
    
#Question 1: Read the tab separated file named "resources/reviews.tsv.gz" into a dataframe.
#You will write this dataframe to S3, define a table on top of it, and use it to answer the same questions from the previous week using SQL
reviews = spark.read.csv("resources/reviews.tsv.gz", sep="\t", header=True)

#Question 2: Add a column to the dataframe named "load_timestamp", representing the current time on your computer. 
with_load_timestamp = reviews.withColumn("load_timestamp", current_timestamp())

#Question 3: Write the dataframe with load timestamp to s3a://hwe-HANDLE/bronze/reviews in Parquet format.
with_load_timestamp.write \
   .mode("overwrite") \
    .parquet("s3a://hwe-tsagona/bronze/reviews/")

#Question 4: Create a table on top of the reviews directory matchiing the schema from the file.
spark.sql("DROP TABLE IF EXISTS hwe.tim_bronze_reviews")
spark.sql("""
CREATE EXTERNAL TABLE hwe.tim_bronze_reviews (
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
review_date string,
load_timestamp timestamp)
STORED AS PARQUET
LOCATION
  's3a://hwe-tsagona/bronze/reviews'
""")

#Answer all questions below using Spark SQL instead of the Python API.

#For all questions, either approach to printing the answer is fine:
#print(result.first()[0])
# or
#result.show()

##Question 3: How many records are in the reviews dataframe? 
result = spark.sql("SELECT count(*) FROM hwe.tim_bronze_reviews")
result.show()

##Question 4: Print the first 5 rows of the dataframe. 
##Some of the columns are long - print the entire record, regardless of length.
result = spark.sql("SELECT * FROM hwe.tim_bronze_reviews LIMIT 5")
result.show(truncate=False)

##Question 5: Create a new dataframe based on "reviews" with exactly 1 column: the value of the product category field.
##Look at the first 50 rows of that dataframe. 
##Which value appears to be the most common?
just_product_category = spark.sql("SELECT product_category from hwe.tim_bronze_reviews LIMIT 50")
just_product_category.show(n=50)

##Question 6: Find the most helpful review in the dataframe - the one with the highest number of helpful votes.
#What is the product title for that review? How many helpful votes did it have?
most_helpful = spark.sql("SELECT product_title, helpful_votes from hwe.tim_bronze_reviews ORDER BY helpful_votes desc LIMIT 1")
most_helpful.show(truncate=False)

##Question 7: How many reviews exist in the dataframe with a 5 star rating?
five_star_reviews = spark.sql("SELECT count(*) from hwe.tim_bronze_reviews where star_rating = \"5\"")
five_star_reviews.show()

##Question 8: Find the date with the most reviews written.
##Print the date and total count of the date where the most reviews were written
review_date_and_count = spark.sql("SELECT review_date, count(*) from hwe.tim_bronze_reviews GROUP BY review_date ORDER BY count(*) DESC LIMIT 1")
review_date_and_count.show()

## Stop the SparkSession
spark.stop()
