# Hours with Experts - Week 6: Building the Gold Layer 

## Introduction

This week, we're going to write a Python program that:

   * reads in AWS credential information from environment variables which allows us to connect to S3
   * creates a `SparkSession` object representing a connection to a local Spark cluster, with parameters that allow us to:
      * connect to S3
      * use 3rd party jars/libraries to interact with S3
   * defines a `Schema` object describing the layout of the Parquet silver review data on S3
   * defines a streaming dataframe from the S3 directory representing the silver layer review data 
   * adds a watermark to that streaming dataframe 
   * uses `groupBy` functionality to summarize that data over any dimensions you may find interesting
   * creates a gold layer by saving that data as Parquet files to S3

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
5. Write that aggregate data to S3 under `s3a://hwe-$CLASS/$HANDLE/gold/fact_review` using append mode and a checkpoint location of `/tmp/gold-checkpoint`

### Teardown
We will wait on the query to terminate for you going forward.
We will stop the `SparkSession` for you going forward.
