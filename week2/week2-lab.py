from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
from pyspark.sql.functions import current_timestamp


# Create a SparkSession
spark = SparkSession.builder.appName("Week2Lab").getOrCreate()

#Question 1: Read the tab separated file named "week2/reviews.tsv" into a dataframe.
<<<<<<< HEAD
#You will use the "df" dataframe defined here to answer all the questions below...
df = None
=======
df = spark.read.csv("week2/reviews.tsv.gz", sep="\t", header=True)
>>>>>>> 172762e... Adding week 2 solution

#Question 2: Display the schema of the dataframe.
df.printSchema()

#Question 3: How many records are in the dataframe? 
#Store this number in a variable named "count".
count = df.count()
print(f"Number of records is {count}")

#Question 4: Print the first 5 rows of the dataframe. 
#Some of the columns are long - print the entire record, regardless of length.
df.show(n=5, truncate=False)

#Question 5: Create a new dataframe based on "df" with exactly 1 column: the value of the product category field.
#Look at the first 50 rows of that dataframe. 
#Which value appears to be the most common?
just_product_category = df.select("product_category")
just_product_category.show(n=50)

#Question 6: Find the most helpful review in the dataframe - the one with the highest number of helpful votes.
#What is the product title for that review?
<<<<<<< HEAD
product_title_and_votes = None
=======
product_title_and_count = df.sort(desc("helpful_votes")).select("product_title", "helpful_votes")
#Either is fine:
product_title_and_count.show(n=1, truncate=False)
#or
print(product_title_and_count.first())
>>>>>>> 172762e... Adding week 2 solution

#Question 7: How many reviews exist in the dataframe with a 5 star rating?
five_star_reviews = df.filter(df.star_rating == "5").count()
print(f"Number of five star reviews = {five_star_reviews}")

#Question 8: Find the date with the most reviews written.
#Print the date and total count of the date where the most reviews were written
review_date_and_count = df.groupBy("review_date").count().sort(desc("count"))
#Either is fine:
review_date_and_count.show(n=1, truncate=False)
#or:
print(review_date_and_count.first())


#Question 9: Add a column to the dataframe named "load_timestamp", representing the current time on your computer. 
#Print the schema and inspect a few rows of data to make sure the data is correctly populated.
with_load_timestamp = df.withColumn("load_timestamp", current_timestamp())
with_load_timestamp.printSchema()

# Stop the SparkSession
spark.stop()
