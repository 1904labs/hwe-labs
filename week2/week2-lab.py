from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
from pyspark.sql.functions import current_timestamp


# Create a SparkSession
spark = SparkSession.builder.appName("Week2Lab").getOrCreate()

#Question 1: Read the tab separated file named "week2/reviews.tsv" into a dataframe.
df = None

#You will use the "df" dataframe defined above to answer all the questions below...

#Question 2: Display the schema of the dataframe.

#Question 3: How many records are in the dataframe? 
#Store this number in a variable named "count".
count = None
print(f"Number of records is {count}")

#Question 4: Print the first 5 rows of the dataframe. 
#Some of the columns are long - print the entire record, regardless of length.

#Question 5: Create a new dataframe with exactly 1 column: the value of the product category field.
#Look at the first 50 rows of that dataframe. 
#Which value appears to be the most common?
just_product_category = None

#Question 6: Find the most helpful review in the dataframe - the one with the highest number of helpful votes.
#What is the product title for that review?
product_title_and_count = None

#Question 7: How many reviews exist in the dataframe with a 5 star rating?
five_star_reviews = None
print(f"Number of five star reviews = {five_star_reviews}")

#Question 8: Find the date with the most reviews written.
#Print the date and total count of the date where the most reviews were written
review_date_and_count = None

#Question 9: Add a column to the dataframe named "load_timestamp", representing the current time on your computer. 
#Print the schema and inspect a few rows of data to make sure the data is correctly populated.
with_load_timestamp = None

# Stop the SparkSession
spark.stop()
