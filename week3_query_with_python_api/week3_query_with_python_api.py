import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc, col
from pyspark.sql.functions import current_timestamp


aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.environ.get("AWS_SESSION_TOKEN")

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Week3Lab") \
    .config("spark.sql.shuffle.partitions", "3") \
    .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider') \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.access.key", aws_access_key_id) \
    .config("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key) \
    .config("spark.hadoop.fs.s3a.session.token", aws_session_token) \
    .config("spark.sql.catalogImplementation", "hive") \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3,org.apache.hadoop:hadoop-aws:3.2.0,com.amazonaws:aws-java-sdk-bundle:1.11.375') \
    .enableHiveSupport()\
    .getOrCreate()

#For Windows users, quiet errors about not being able to delete temporary directories which make your logs impossible to read...
logger = spark.sparkContext._jvm.org.apache.log4j
logger.LogManager.getLogger("org.apache.spark.util.ShutdownHookManager"). setLevel( logger.Level.OFF )
logger.LogManager.getLogger("org.apache.spark.SparkEnv"). setLevel( logger.Level.ERROR )

#Question 1: Read the tab separated file named "resources/reviews.tsv.gz" into a dataframe.
#You will use the "reviews" dataframe defined here to answer all the questions below...
reviews = spark.read.csv("resources/reviews.tsv.gz", sep="\t", header=True)

#Question 2: Display the schema of the dataframe.
reviews.printSchema()

#Question 3: How many records are in the dataframe? 
#Store this number in a variable named "reviews_count".
reviews_count = reviews.count()
print(f"Number of records is {reviews_count}")

#Question 4: Print the first 5 rows of the dataframe. 
#Some of the columns are long - print the entire record, regardless of length.
reviews.show(n=5, truncate=False)

#Question 5: Create a new dataframe based on "reviews" with exactly 1 column: the value of the product category field.
#Look at the first 50 rows of that dataframe. 
#Which value appears to be the most common?
just_product_category = reviews.select("product_category")
just_product_category.show(n=50)

#Question 6: Find the most helpful review in the dataframe - the one with the highest number of helpful votes.
#What is the product title for that review? How many helpful votes did it have?
product_title_and_votes = reviews.sort(desc("helpful_votes")).select("product_title", "helpful_votes")
#Either is fine:
product_title_and_votes.show(n=1, truncate=False)
#or
print(product_title_and_votes.first())

#Question 7: How many reviews have a 5 star rating?
five_star_reviews = reviews.filter(reviews.star_rating == "5").count()
print(f"Number of five star reviews = {five_star_reviews}")

#Question 8: Currently every field in the data file is interpreted as a string, but there are 3 that should really be numbers.
#Create a new dataframe with just those 3 columns, except cast them as "int"s.
#Look at 10 rows from this dataframe.
int_columns = reviews.select(col("star_rating").cast('int'), col("helpful_votes").cast("int"), col("total_votes").cast("int"))
#or
int_columns = reviews.selectExpr("cast(star_rating as int)", "cast(helpful_votes as int)", "cast(total_votes as int)")
int_columns.show(n=10)


#Question 8: Find the date with the most purchases.
#Print the date and total count of the date with the most purchases
purchase_date_and_count = reviews.groupBy("purchase_date").count().sort(desc("count"))
#Either is fine:
purchase_date_and_count.show(n=1, truncate=False)
#or:
print(purchase_date_and_count.first())


#Question 9: Add a column to the dataframe named "review_timestamp", representing the current time on your computer. 
#Print the schema and inspect a few rows of data to make sure the data is correctly populated.
with_review_timestamp = reviews.withColumn("review_timestamp", current_timestamp())
with_review_timestamp.printSchema()

#Question 10: Write the dataframe with load timestamp to s3a://hwe-HANDLE/bronze/reviews in Parquet format.
with_review_timestamp.write \
   .mode("overwrite") \
   .parquet("s3a://hwe-tsagona/bronze/reviews/")

#Question 11: Read the tab separated file named "resources/customers.tsv.gz" into a dataframe
#Write to S3 under s3a://BUCKET/path/bronze/customers
#There are no questions to answer about this dat set right now, but you will use it in a later lab...
customers = spark.read.csv("resources/customers.tsv.gz", sep="\t", header=True)
customers.write \
    .mode("overwrite") \
    .parquet("s3a://hwe-tsagona/bronze/customers")

# Stop the SparkSession
spark.stop()
