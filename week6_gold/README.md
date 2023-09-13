# Hours with Experts - Week 6: Building the Gold Layer 

## Introduction

**Important**: This lab is going to use watermarks, which is a feature of Spark that is not supported using Spark SQL. You *must* use the Spark DataFrame API to complete this lab!

This week, we're going to write a Python program that:

   * reads in AWS credential information from environment variables which allows us to connect to S3
   * creates a `SparkSession` object representing a connection to a local Spark cluster, with parameters that allow us to:
      * connect to S3
      * use 3rd party jars/libraries to interact with S3
   * defines a `Schema` object describing the layout of the silver review data
   * defines a streaming dataframe from the S3 directory representing the silver layer review data 
   * adds a watermark to that streaming dataframe 
   * uses `groupBy` functionality to summarize that data over any dimensions you may find interesting
   * creates a gold layer by saving that data to S3 using "delta" format

## Assignment

### Setup

We will define Python variables which read the values of environment variables which need to be set to:
   * AWS_ACCESS_KEY_ID = the valid, recently acquired, temporary AWS access key for your IAM user
   * AWS_SECRET_ACCESS_KEY = the valid, recently acquired, temporary AWS secret access key for your IAM user
   * AWS_SESSION_TOKEN = the valid, recently acquired, temporary AWS session for your IAM user

We will define the `SparkSession` for you, since some of the parameters get complex.

### Questions

1. Define a `silver_schema` which describes the Parquet files under the silver reviews directory on S3
2. Define a streaming dataframe using `readStream` on top of the silver reviews directory on S3
3. Define a `watermarked_data` dataframe by defining a watermark on the `review_timestamp` column with an interval of 10 seconds
4. Define an aggregated dataframe using `groupBy` functionality to summarize that data over any dimensions you may find interesting
5. Write that aggregate data to S3 under `s3a://hwe-$CLASS/$HANDLE/gold/fact_review` using append mode, a checkpoint location of `/tmp/gold-checkpoint`, and a format of `delta`
6. Outside of this program, create a table on top of your S3 data in Athena, and run some queries against your data to validate it is coming across the way you expect. Since you get to choose what your gold layer table will look like, you get to decide what fields are necessary to validate!

### Teardown
We will wait on the query to terminate for you going forward.
We will stop the `SparkSession` for you going forward.
