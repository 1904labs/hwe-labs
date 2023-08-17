# Hours with Experts - Week 4: Spark Structured Streaming from Kafka

## Introduction

This week, we're going to write a Python program that:

   * reads in AWS credential information from environment variables which allows us to connect to S3
   * reads in the bootstrap servers, username, and password from environment variables for a Kafka cluster hosted on AWS
   * creates a `SparkSession` object representing a connection to a local Spark cluster, with parameters that allow us to:
      * connect to S3
      * use 3rd party jars/libraries to interact with S3
   * uses that `SparkSession` to read a stream of data from Kafka
   * reads and transforms data from Kafka
   * writes that data to S3
   * waits on the streaming query to terminate

## Assignment

### Setup

We will define Python variables which read the values of environment variables which need to be set to:
   * HWE_BOOTSTRAP = the address of the HWE Kafka cluster
   * HWE_USERNAME = the username used to authenticate to the HWE Kafka cluster (ask a TA)
   * HWE_PASSWORD = the password used to authenticate to the HWE Kafka cluster (ask a TA)
   * AWS_ACCESS_KEY_ID = the valid, recently acquired, temporary AWS access key for your IAM user
   * AWS_SECRET_ACCESS_KEY = the valid, recently acquired, temporary AWS secret access key for your IAM user
   * AWS_SESSION_TOKEN = the valid, recently acquired, temporary AWS session for your IAM user

We will define the name of the Kafka topic containing review data (`reviews`)

We will define the `SparkSession` for you, since some of the parameters get complex.

We will start you off by setting up the necessary parameters for Spark to connect to the HWE Kafka cluster, since some of the parameters get complex.

### Questions

Modify the `df` dataframe defined in the lab to do the following:

   * split the value of the Kafka message on tab characters, assigning a field name to each element using the `as` keyword
   * append a column to the data named `review_timestamp` which is set to the current_timestamp
   * write that data as Parquet files to S3 using append mode

### Teardown
We will wait on the query to terminate for you going forward.
We will stop the `SparkSession` for you going forward.
