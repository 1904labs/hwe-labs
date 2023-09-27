import os
import shutil
from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructType, StructField

'''
Tests environment can run a spark app and load a dataframe
'''
def spark_df_test(spark: SparkSession):
    ## ARRANGE
    # Define the data
    data = [("Congratulations! You have successfully executed a Spark application written in Python!",)]

    # Define the schema for the DataFrame
    #schema = StringType()
    schema  = StructType([
        StructField("message", StringType(), True)
    ])

    ## ACT
    # Create a DataFrames
    df: DataFrame = spark.createDataFrame(data, schema)

    # Print the DataFrame
    df.show(truncate=False)
    ## ASSERT w/ visual inspection

'''
Tests environment can load a CSV file and write to a JSON file
'''
def spark_file_io_test(spark: SparkSession):
    ## ARRANGE - if we see evidence of already having been run, delete the contents for a clean test
    src_file_path: str = os.path.abspath("resources/file_io_test.csv")
    dest_folder_path: str = os.path.abspath("resources/file_io_test_json")
    if (os.path.exists(dest_folder_path)):
        shutil.rmtree(dest_folder_path)

    ## ACT
    df: DataFrame = spark.read.csv(src_file_path)
    df.write.json(dest_folder_path)

    ## ASSERT - if folder exists and has files, calling it good enough
    if (os.path.exists(dest_folder_path) and any(os.listdir(dest_folder_path))):
        # Party on Wayne
        print("And even better yet, you can read from and write to storage!")
    else:
        # I'm no worthy
        print("Unfortunately the file IO ops did not work as expected.\r\n" +
              "Consider working through the `setup-<your device type>.md` instructions again.")

# Create a SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkInstallationTest").getOrCreate()

# Test running bare minimum Spark + Python app
spark_df_test(spark)

# Now test file operations
spark_file_io_test(spark)

# Stop the SparkSession
spark.stop()