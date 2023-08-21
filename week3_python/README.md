# Hours with Experts - Week 3: Spark using Python

## Introduction

This week, we're going to write a Python program that:

   * reads in AWS credential information from environment variables which allows us to connect to S3
   * creates a `SparkSession` object representing a connection to a local Spark cluster, with parameters that allow us to:
      * connect to S3
      * use 3rd party jars/libraries to interact with S3
   * uses that `SparkSession` to reads in a local file containing (real) Amazon review data
   * queries that data using the Python Spark SQL API
   * writes that data to S3
   * stops our `SparkSession`

## Setting up AWS environment variables

Note: from this point forward in the course, we will be connecting to various resources hosted on AWS. In order to successfully connect you will need to set several environment variables on your machine.

### Access Key, Secret Key, and Session Token

You will be authenticating to AWS using temporary security credentials you will obtain from signing on via the AWS console. These temporary credentials will expire after 12 hours, at which point you will need to re-generate new ones.

To get your credentials:

1. Sign onto the AWS console.
2. Click "Command line or programmatic access"

We need to set 3 environment variables on your machine:
   * AWS_ACCESS_KEY_ID - set this to the value of `AWS Access Key ID` from the screen above
   * AWS_SECRET_ACCESS_KEY - set this to the value of `AWS Secret Access Key` from the screen above
   * AWS_SESSION_TOKEN - set this to the value of `AWS Session Token` from the screen above

**Important**: Any time you update environment variables, you will need to close and re-open all command prompts, all VS Code instances, etc. They will *not* automatically pick up changes to your environment.

For example, if you run your program and then realize your credentials have expired, it's not enough to simply obtain new creds, update your variables with the new values, and re-run. You must:
   * obtain new credentials
   * update your environment variables
   * close all terminals, editors, etc.
   * relaunch all terminals, editors, etc.
   * re-run your application

## Assignment

### Setup

We will define Python variables which read the values of environment variables which need to be set to:
   * AWS_ACCESS_KEY_ID = the valid, recently acquired, temporary AWS access key for your IAM user
   * AWS_SECRET_ACCESS_KEY = the valid, recently acquired, temporary AWS secret access key for your IAM user
   * AWS_SESSION_TOKEN = the valid, recently acquired, temporary AWS session for your IAM user

We will define the `SparkSession` for you going forward, since some of the parameters get complex from here.

### Questions

1. Read the tab separated file named `resources/reviews.tsv.gz` into a dataframe. Call it `reviews`. You will use the `reviews` dataframe defined here to answer all the questions below...

2. Display the schema of the dataframe.

3. How many records are in the dataframe? Store this number in a variable named `reviews_count`.

4. Print the first 5 rows of the dataframe. Some of the columns are long - print the entire record, regardless of length.

5. Create a new dataframe based on `reviews` with exactly 1 column: the value of the product category field. Look at the first 50 rows of that dataframe. Which value appears to be the most common?

6. Find the most helpful review in the dataframe - the one with the highest number of helpful votes What is the product title for that review? How many helpful votes did it have?

7. How many reviews have a 5 star rating?

8. Currently every field in the data file is interpreted as a string, but there are 3 that should really be numbers. Create a new dataframe with just those 3 columns, except cast them as `int`s. Look at 10 rows from this dataframe.

9. Find the date with the most purchases. Print the date and total count of the date with the most purchases

10. Add a column to the dataframe named `review_timestamp`, representing the current time on your computer. Print the schema and inspect a few rows of data to make sure the data is correctly populated.

11. Write the dataframe with load timestamp to `s3a://hwe-$CLASS/$HANDLE/bronze/reviews_static` in Parquet format.

12. Read the tab separated file named `resources/customers.tsv.gz` into a dataframe. Write to S3 under `s3a://hwe-$CLASS/$HANDLE/bronze/customers`. There are no questions to answer about this data set right now, but you will use it in a later lab...

### Teardown
We will stop the `SparkSession` for you going forward.
