import os
from kafka import KafkaConsumer
from tabulate import tabulate

# Load environment variables.
from dotenv import load_dotenv
load_dotenv()

# Kafka broker details
bootstrap_servers = os.environ.get("HWE_BOOTSTRAP")
username = os.environ.get("HWE_USERNAME")
password = os.environ.get("HWE_PASSWORD")

# Kafka topic to consume messages from
topic = 'demo-topic-1'

# Create Kafka consumer
consumer = KafkaConsumer(topic,
                         group_id='demo-group',
                         security_protocol="SASL_SSL",
                         sasl_mechanism="SCRAM-SHA-512", 
                         sasl_plain_username=username, 
                         sasl_plain_password=password, 
                         bootstrap_servers=bootstrap_servers,
                         auto_offset_reset="earliest")

# We are going to print the data from Kafka in a table
# Define the table headers
headers = ["Topic", "Partition", "Offset", "Key", "Value"]

# Continuously poll for messages
for message in consumer:
    data = [
        message.topic,
        message.partition,
        message.offset,
        message.key,
        message.value.decode('utf-8')
    ]
    table = [headers, data]
    print(tabulate(table, headers="firstrow", tablefmt="pretty"))

# Close the consumer (this will not be reached)
consumer.close()
