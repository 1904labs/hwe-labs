# Hours with Experts - Week 5: Joining 

## Introduction

This week, we're going to write a Python program that uses Spark SQL (not the DataFrame API):

   * reads in AWS credential information from environment variables which allows us to connect to S3
   * creates a `SparkSession` object representing a connection to a local Spark cluster, with parameters that allow us to:
      * connect to S3
      * use 3rd party jars/libraries to interact with S3
   * defines a dataframe `schema` describing the layout of the bronze data written by our bronze pipeline
   * defines a streaming dataframe from the S3 directory representing the bronze layer review data 
   * defines a virtual view on that dataframe we can query using Spark SQL
   * defines a static dataframe from the S3 directory representing the bronze layer customer data
   * defines a virtual view on that dataframe we can query using Spark SQL
   * defines a streaming dataframe by joining the review and customer data on their common key of `customer_id`
   * write that data as Parquet files to S3 using append mode

## Assignment

### Setup

We will define Python variables which read the values of environment variables which need to be set to:
   * AWS_ACCESS_KEY_ID = the valid, recently acquired, temporary AWS access key for your IAM user
   * AWS_SECRET_ACCESS_KEY = the valid, recently acquired, temporary AWS secret access key for your IAM user
   * AWS_SESSION_TOKEN = the valid, recently acquired, temporary AWS session for your IAM user

We will define the `SparkSession` for you, since some of the parameters get complex.

### Questions

1. Define a `bronze_schema` which describes the Parquet files under the bronze reviews directory on S3
2. Define a streaming dataframe using `readStream` on top of the bronze reviews directory on S3
3. Register a virtual view on top of that dataframe
4. Define a non-streaming dataframe using `read` on top of the bronze customers directory on S3
5. Register a virtual view on top of that dataframe
6. Define a `silver_data` dataframe by joining the review and customer data on their common key of `customer_id`
7. Write that silver data to S3 under `s3a://hwe-$CLASS/$HANDLE/silver/reviews` using append mode and a checkpoint location of `/tmp/silver-checkpoint`
8. Outside of this program, create a table on top of your S3 data in Athena, and run some queries against your data to validate it is coming across the way you expect. Some useful fields to validate could include:

   * product_title
   * star_rating
   * review_timestamp
   * customer_name
   * gender
   * city
   * state

GROUP BY and LIMIT are also useful here.

### Teardown
We will wait on the query to terminate for you going forward.
We will stop the `SparkSession` for you going forward.
