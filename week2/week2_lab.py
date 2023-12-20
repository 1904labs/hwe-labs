####### Welcome to the Week 2 Lab!
# Go throug the following exercises where we learn about
# PySparks SQL and DataFrame APIs.  In addition we will learn
# the difference between Spark Transforms and Actions.

####### import libraries and setup environment
from pyspark.sql import SparkSession, DataFrame

####### perform environment tests
# TODO section

####### setup environment

# Create a SparkSession
spark = None

# For Windows users, quiet errors about not being able to delete temporary directories which make your logs impossible to read...
if not spark is None:
    logger = spark.sparkContext._jvm.org.apache.log4j
    logger.LogManager.getLogger("org.apache.spark.util.ShutdownHookManager"). setLevel( logger.Level.OFF )
    logger.LogManager.getLogger("org.apache.spark.SparkEnv"). setLevel( logger.Level.ERROR )

### Challeneges and Questions

# Note - some of these challenges/questions are asking you to do the same thing twice, with two 
#           different PySPark APIs. Please complete those challenges with both PySpark APIs
#           verify you get the same answer. The challenges that are asking for to use the two APIs 
#           will be in the following format:
## Challenge X: <challenge content>
# With SQL
# With DataFrame

## Challenge 1: Read the tab separated file named "resources/reviews.tsv.gz" into a dataframe and 
# name the variable 'reviews'.  For this homework it's important that you don't use the infer 
# schema option when reading the file.
reviews = None

# Question 1.1: What type of character seperates the content of each rows?
# Question 1.2: Why might a data engineer NOT want to infer the schema? 

## Challenge 2: Print the first 5 rows of the dataframe. 
# Some of the columns are long - print the entire record, regardless of length.


## Challenge 3: Print the schema and verify that all columns are strings and 
# the following columns are found in the DataFrame:
#


## Challenge 4: Create a virtual view on top of the reviews dataframe, so that we can query it with Spark SQL.
# Name the virtual view 'reviews_view' for future referencing.


## Challenge 5: Determine the number of records in the 'reviews_view' view and the 'reviews' dataframe. 
# With SQL - use 'reviews_view'
# With DataFrame - use 'reviews' dataframe

# Question 5.1: How many records are there?


## Challenge 6: Create a new dataframe based on "reviews" with exactly 1 column, the: the value 
# of the 'product_category' field. Determine the 'product_category' that is most common.
# With SQL - use 'reviews_view'
# With DataFrame - use 'reviews' dataframe

# Question 6.1: Which value is the most common?


## Challenge 7: Find how many reviews exist in the dataframe with a 5 star rating.
# With SQL - use 'reviews_view'
# With DataFrame - use 'reviews' dataframe
 
# Question 7.1: How many reviews exist in the dataframe with a 5 star rating?


## Challenge 8: Find the most helpful review in the dataframe - the one with 
# the highest number of helpful votes.
# With SQL - use 'reviews_view'
# With DataFrame - use 'reviews' dataframe

# Question 8.1: What is the product title for that review? 
# Question 8.2: How many helpful votes did it have?


## Challenge 9: Find the date with the most purchases.
# With SQL - use 'reviews_view'
# With DataFrame - use 'reviews' dataframe

# Question 9.1: What is the date with the most purchases?
# Question 9.2: What is the count of purchases?


# Challenge 10: Currently every field in the data file is interpreted as a string, 
# but there are 3 that should really be numbers.  Create a new dataframe with just 
# keeping the original columns but casting the 3 columns that should be integers
# as actually ints.


# Challenge 11: Write the dataframe from Challenge 10 to your drive in JSON format.
# Feel free to pick any directory on your computer.
# Use overwrite mode.

### Teardown
# Stop the SparkSession




####### Stretch Challenges

## Stretch Challenge:
# For this stretch challenge you will complete the implementation of the 
# method below implementing all documented aspects of its operation.  To ensure
# this is completed fully, you will execute unit tests that will verify the code
# executes as expected.  To complete this stretch challenge, please complete
# the following:
#   1.  Fill out the method body below
#   2.  Execute the unit tests found in 'test_week2_lab.py'...keep 
#       iterating until all of them pass 

def get_most_frequent_product_categories(df: DataFrame) -> DataFrame:
    '''
    Gets the most frequently occurring values from the String 'product_category'
     column passed into the DataFrame.
    
    Raises:
        ValueError: The DataFrame does not contain a 'product_category' column.
         
    Parameters:
        df (DataFrame): The DataFrame that contains the 'product_category' column.

    Returns:
        A DataFrame with one column named 'product_category' containing only the 
        most frequent 'product_category' values.  If no rows are included in the
        input DataFrame, zero rows are returned in the output DataFrame.   
    '''
    # TODO: fill in with actual implementation    
    return None
