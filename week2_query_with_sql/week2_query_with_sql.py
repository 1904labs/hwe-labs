from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
from pyspark.sql.functions import current_timestamp

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Week2Lab") \
    .config("spark.sql.shuffle.partitions", "3") \
    .config("spark.sql.catalogImplementation", "hive") \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3,org.apache.hadoop:hadoop-aws:3.2.0,com.amazonaws:aws-java-sdk-bundle:1.11.375') \
    .enableHiveSupport()\
    .getOrCreate()

#For Windows users, quiet errors about not being able to delete temporary directories which make your logs impossible to read...
logger = spark.sparkContext._jvm.org.apache.log4j
logger.LogManager.getLogger("org.apache.spark.util.ShutdownHookManager"). setLevel( logger.Level.OFF )
logger.LogManager.getLogger("org.apache.spark.SparkEnv"). setLevel( logger.Level.ERROR )

#Question 1: Read the tab separated file named "resources/reviews.tsv.gz" into a dataframe.
#You will write this dataframe to S3, register it with a name so that it can be used with Spark SQL , and use it to answer the same questions from the previous week using SQL
reviews = spark.read.csv("resources/reviews.tsv.gz", sep="\t", header=True)

#Question 2: Create a table on top of the reviews directory matchiing the schema from the file.
reviews.createOrReplaceTempView("reviews")

#Question 3: Add a column to the dataframe named "review_timestamp", representing the current time on your computer. 
with_review_timestamp = spark.sql("select r.*, current_timestamp() from reviews r")
with_review_timestamp.printSchema()
with_review_timestamp.show()

#Answer all questions below using Spark SQL instead of the Python API.

#For all questions, either approach to printing the answer is fine:
#print(result.first()[0])
# or
#result.show()

##Question 4: How many records are in the reviews dataframe? 
result = spark.sql("SELECT count(*) FROM reviews")
result.show()

##Question 5: Print the first 5 rows of the dataframe. 
##Some of the columns are long - print the entire record, regardless of length.
result = spark.sql("SELECT * FROM reviews LIMIT 5")
result.show(truncate=False)

##Question 6: Create a new dataframe based on "reviews" with exactly 1 column: the value of the product category field.
##Look at the first 50 rows of that dataframe. 
##Which value appears to be the most common?
just_product_category = spark.sql("SELECT product_category from reviews LIMIT 50")
just_product_category.show(n=50)

##Question 7: Find the most helpful review in the dataframe - the one with the highest number of helpful votes.
#What is the product title for that review? How many helpful votes did it have?
most_helpful = spark.sql("SELECT product_title, helpful_votes from reviews ORDER BY helpful_votes desc LIMIT 1")
most_helpful.show(truncate=False)

##Question 8: How many reviews exist in the dataframe with a 5 star rating?
five_star_reviews = spark.sql("SELECT count(*) from reviews where star_rating = \"5\"")
five_star_reviews.show()

#Question 9: Currently every field in the data file is interpreted as a string, but there are 3 that should really be numbers.
#Create a new dataframe with just those 3 columns, except cast them as "int"s.
#Look at 10 rows from this dataframe.
int_columns = spark.sql("select cast(star_rating as int), cast(helpful_votes as int), cast(total_votes as int) from reviews")
int_columns.show(n=10)

##Question 9: Find the date with the most purchases.
##Print the date and total count of the date which had the most purchases.
purchase_date_and_count = spark.sql("SELECT purchase_date, count(*) from reviews GROUP BY purchase_date ORDER BY count(*) DESC LIMIT 1")
purchase_date_and_count.show()

## Stop the SparkSession
spark.stop()
