import time
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructType, StructField

# Create a SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkInstallationTest").getOrCreate()

# Define the data
data = [("Congratulations! The first Spark program is executing!",),("(This program will run until you terminate it...)",)]

# Define the schema for the DataFrame
#schema = StringType()
schema  = StructType([
    StructField("message", StringType(), True)
])

# Create a DataFrames
df = spark.createDataFrame(data, schema)

# Print the DataFrame
df.show(truncate=False)

time.sleep(9999)
# Stop the SparkSession
spark.stop()