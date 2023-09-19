from pyspark.sql import SparkSession

### Setup: Create a SparkSession
spark = SparkSession.builder \
    .appName("Week2Lab") \
    .master('local[*]') \
    .getOrCreate()

# For Windows users, quiet errors about not being able to delete temporary directories which make your logs impossible to read...
logger = spark.sparkContext._jvm.org.apache.log4j
logger.LogManager.getLogger("org.apache.spark.util.ShutdownHookManager"). setLevel( logger.Level.OFF )
logger.LogManager.getLogger("org.apache.spark.SparkEnv"). setLevel( logger.Level.ERROR )

### Questions
# Question 1: Read the tab separated file named "resources/reviews.tsv.gz" into a dataframe. Call it "reviews".
reviews = spark.read.csv("resources/reviews.tsv.gz", sep="\t", header=True)

# Question 2: Create a virtual view on top of the reviews dataframe, so that we can query it with Spark SQL.
reviews.createOrReplaceTempView("reviews")

# Question 3: Add a column to the dataframe named "review_timestamp", representing the current time on your computer. 
with_review_timestamp = spark.sql("select r.*, current_timestamp() from reviews r")
with_review_timestamp.printSchema()
with_review_timestamp.show()

#For all questions, either approach to printing the answer is fine:
#print(result.first()[0])
# or
#result.show()

# Question 4: How many records are in the reviews dataframe? 
result = spark.sql("SELECT count(*) FROM reviews")
result.show()

# Question 5: Print the first 5 rows of the dataframe. 
# Some of the columns are long - print the entire record, regardless of length.
result = spark.sql("SELECT * FROM reviews LIMIT 5")
result.show(truncate=False)

# Question 6: Create a new dataframe based on "reviews" with exactly 1 column: the value of the product category field.
# Look at the first 50 rows of that dataframe. 
# Which value appears to be the most common?
just_product_category = spark.sql("SELECT product_category from reviews LIMIT 50")
just_product_category.show(n=50)

# Question 7: Find the most helpful review in the dataframe - the one with the highest number of helpful votes.
# What is the product title for that review? How many helpful votes did it have?
most_helpful = spark.sql("SELECT product_title, helpful_votes from reviews ORDER BY helpful_votes desc LIMIT 1")
most_helpful.show(truncate=False)

# Question 8: How many reviews exist in the dataframe with a 5 star rating?
five_star_reviews = spark.sql("SELECT count(*) from reviews where star_rating = \"5\"")
five_star_reviews.show()

# Question 9: Currently every field in the data file is interpreted as a string, but there are 3 that should really be numbers.
# Create a new dataframe with just those 3 columns, except cast them as "int"s.
# Look at 10 rows from this dataframe.
int_columns = spark.sql("select cast(star_rating as int), cast(helpful_votes as int), cast(total_votes as int) from reviews")
int_columns.show(n=10)

# Question 10: Find the date with the most purchases.
# Print the date and total count of the date which had the most purchases.
purchase_date_and_count = spark.sql("SELECT purchase_date, count(*) from reviews GROUP BY purchase_date ORDER BY count(*) DESC LIMIT 1")
purchase_date_and_count.show()

##Question 11: Write the dataframe from Question 3 to your drive in JSON format.
##Feel free to pick any directory on your computer.
##Use overwrite mode.
with_review_timestamp.write \
.mode("overwrite") \
.json("resources/tim_json")

### Teardown
# Stop the SparkSession
spark.stop()
