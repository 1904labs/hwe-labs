from pyspark.sql import SparkSession

# Setup: Create a SparkSession
spark = None

#For Windows users, quiet errors about not being able to delete temporary directories which make your logs impossible to read...
logger = spark.sparkContext._jvm.org.apache.log4j
logger.LogManager.getLogger("org.apache.spark.util.ShutdownHookManager"). setLevel( logger.Level.OFF )
logger.LogManager.getLogger("org.apache.spark.SparkEnv"). setLevel( logger.Level.ERROR )

#Question 1: Read the tab separated file named "resources/reviews.tsv.gz" into a dataframe. Call it "reviews".

#Question 2: Create a virtual view on top of the reviews dataframe, so that we can query it with Spark SQL.

#Question 3: Add a column to the dataframe named "review_timestamp", representing the current time on your computer. 

##Question 4: How many records are in the reviews dataframe? 

##Question 5: Print the first 5 rows of the dataframe. 
##Some of the columns are long - print the entire record, regardless of length.

##Question 6: Create a new dataframe based on "reviews" with exactly 1 column: the value of the product category field.
##Look at the first 50 rows of that dataframe. 
##Which value appears to be the most common?

##Question 7: Find the most helpful review in the dataframe - the one with the highest number of helpful votes.
#What is the product title for that review? How many helpful votes did it have?

##Question 8: How many reviews exist in the dataframe with a 5 star rating?

#Question 9: Currently every field in the data file is interpreted as a string, but there are 3 that should really be numbers.
#Create a new dataframe with just those 3 columns, except cast them as "int"s.
#Look at 10 rows from this dataframe.

##Question 10: Find the date with the most purchases.
##Print the date and total count of the date which had the most purchases.

##Question 11: Write the dataframe from Question 3 to your drive in JSON format.
##Feel free to pick any directory on your computer.
##Use overwrite mode.

## Stop the SparkSession
