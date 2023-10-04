from pyspark.sql import SparkSession
from pyspark.sql.types import StringType

# Load environment variables.
from dotenv import load_dotenv
load_dotenv()

def getScramAuthString(username, password):
  return f"""org.apache.kafka.common.security.scram.ScramLoginModule required
   username="{username}"
   password="{password}";
   """

# Create a SparkSession
spark = SparkSession.builder \
    .appName("SimpleProducer") \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1') \
    .config("spark.sql.shuffle.partitions", "3") \
    .getOrCreate()

# Define the Kafka broker and topic to read from
kafka_bootstrap_servers = "b-2-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196,b-1-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196,b-3-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196"
kafka_topic = "timsagona"
username = "1904labs"
password= "1904labs"
truststore = "week3/kafka.client.truststore.jks"

# Create SparkSession
spark = SparkSession.builder \
    .appName("SimpleProducer") \
    .getOrCreate()

# Create a sample dataframe with a message column
data = [("Hello from Pyspark")]
df = spark.createDataFrame(data, StringType()).toDF("message")

# Write dataframe to Kafka
df.selectExpr("CAST(null as STRING) as key", "CAST(message AS STRING) as value") \
    .write \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers)\
    .option("kafka.security.protocol", "SASL_SSL")\
    .option("kafka.sasl.mechanism", "SCRAM-SHA-512")\
    .option("kafka.sasl.jaas.config", getScramAuthString(username, password))\
    .option("kafka.enable.idempotence", "false")\
    .option("topic", kafka_topic) \
    .save()

# Trigger Spark job execution
spark.stop()

