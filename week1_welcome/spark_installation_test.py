from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructType, StructField

# Create a SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkInstallationTest").getOrCreate()

# Define the data
data = [("Congratulations! You have successfully executed a Spark application written in Python!",)]

# Define the schema for the DataFrame
#schema = StringType()
schema  = StructType([
    StructField("message", StringType(), True)
])

# Create a DataFrames
df = spark.createDataFrame(data, schema)

# Print the DataFrame
df.show(truncate=False)

# Stop the SparkSession
spark.stop()