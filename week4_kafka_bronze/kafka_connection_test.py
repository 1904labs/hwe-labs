import os
from kafka import KafkaConsumer

# Load environment variables.
from dotenv import load_dotenv
load_dotenv()

def getScramAuthString(username, password):
  return f"""org.apache.kafka.common.security.scram.ScramLoginModule required
   username="{username}"
   password="{password}";
  """

# Kafka broker address and port
kafka_bootstrap_servers = os.environ.get("HWE_BOOTSTRAP")
username = os.environ.get("HWE_USERNAME")
password = os.environ.get("HWE_PASSWORD")

# Kafka topic to read from
topic = 'kafka-connection-test'

# Create a KafkaConsumer instance
consumer = KafkaConsumer(topic,
                         bootstrap_servers=kafka_bootstrap_servers,
                         auto_offset_reset='earliest',  # Read from the beginning of the topic
                         security_protocol='SASL_SSL',
                         sasl_mechanism='SCRAM-SHA-512',
                         sasl_plain_username=username,
                         sasl_plain_password=password
                         )
try:
    # Poll and read messages from the topic
    for message in consumer:
        # Decode the message value assuming it is a string
        message_value = message.value.decode('utf-8')
        print(f"{message_value}")

except KeyboardInterrupt:
    # Handle keyboard interruption (e.g., Ctrl+C) to gracefully stop the consumer
    print("Consumer interrupted. Closing the consumer.")
finally:
    # Close the Kafka consumer to release resources
    consumer.close()
