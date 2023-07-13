from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp


def getScramAuthString(username, password):
  return f"""org.apache.kafka.common.security.scram.ScramLoginModule required
   username="{username}"
   password="{password}";
  """

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Week3Lab") \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1') \
    .config("spark.sql.shuffle.partitions", "3") \
    .getOrCreate()

# Define the Kafka broker and topic to read from
kafka_bootstrap_servers = "b-2-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196,b-1-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196,b-3-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196"
kafka_topic = "timsagona"
username = "1904labs"
password= "1904labs"

# Read data from Kafka using the DataFrame API
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", "earliest") \
    .option("kafka.security.protocol", "SASL_SSL") \
    .option("kafka.sasl.mechanism", "SCRAM-SHA-512") \
    .option("kafka.sasl.jaas.config", getScramAuthString(username, password)) \
    .load() \
    .select("key", col("value").cast("string"), "topic", "partition", "offset", "timestamp", "timestampType") \
    .withColumn("load_timestamp", current_timestamp())
#.selectExpr("key", "CAST(value AS STRING)", "topic", "partition", "offset", "timestamp", "timestampType") 
    

# Process the received data
query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start()

# Wait for the streaming query to finish
query.awaitTermination()
