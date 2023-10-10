import os
from kafka import KafkaProducer
import time

# Load environment variables.
from dotenv import load_dotenv
load_dotenv()

# Kafka broker details
bootstrap_servers = os.environ.get("HWE_BOOTSTRAP")
username = os.environ.get("HWE_USERNAME")
password = os.environ.get("HWE_PASSWORD")

# Kafka topic to produce messages to
topic = 'demo-topic-1'

# Create Kafka producer
producer = KafkaProducer(security_protocol="SASL_SSL",
                           sasl_mechanism="SCRAM-SHA-512", 
                           sasl_plain_username=username, 
                           sasl_plain_password=password, 
                           bootstrap_servers=bootstrap_servers)

for i in range(0,10):
    # Define the message
    message = str(i)*5
    # Produce the message to the topic
    producer.send(topic, value=message.encode('utf-8'))
    # Flush the producer to ensure the message is sent
    producer.flush()

# Close the producer
producer.close()
