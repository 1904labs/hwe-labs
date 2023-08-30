# Hours with Experts - Week 2: Spark using SQL

## Assignment Instructions

This week, we're going to write a Python program that:

   * creates a `SparkSession` object representing a connection to a local Spark cluster
   * uses that `SparkSession` to read a local file containing (real) Amazon review data
   * defines a virtual view we can query using Spark SQL
   * uses that view to answer questions about the data
   * stops our `SparkSession`

All of the following sections in this README can be found in 'week2_query_with_sql.py'.  Your assignment is to go through the following sections in '[week2_query_with_sql.py](week2_query_with_sql.py)' and write the code to complete the task for the corresponding comment.

### Setup 
Create a `SparkSession` object representing a connection to a local Spark cluster

### Questions

1. Read the tab separated file named `resources/reviews.tsv.gz` into a dataframe. Call it `reviews`.

2. Create a virtual view on top of the reviews dataframe, so that we can query it with Spark SQL.

3. Add a column to the dataframe named `review_timestamp`, representing the current time on your computer. 

4. How many records are in the reviews dataframe? 

5. Print the first 5 rows of the dataframe. Some of the columns are long - print the entire record, regardless of length.

6. Create a new dataframe based on `reviews` with exactly 1 column: the value of the product category field. Look at the first 50 rows of that dataframe. Which value appears to be the most common?

7. Find the most helpful review in the dataframe - the one with the highest number of helpful votes. What is the product title for that review? How many helpful votes did it have?

8. How many reviews exist in the dataframe with a 5 star rating?

9. Currently every field in the data file is interpreted as a string, but there are 3 that should really be numbers. Create a new dataframe with just those 3 columns, except cast them as `int`s. Look at 10 rows from this dataframe.

10. Find the date with the most purchases. Print the date and total count of the date which had the most purchases.

### Teardown 
Stop the `SparkSession`
