import os
from kafka import KafkaProducer

# Load environment variables.
from dotenv import load_dotenv
load_dotenv()

# Kafka broker details
bootstrap_servers = os.environ.get("HWE_BOOTSTRAP")
username = os.environ.get("HWE_USERNAME")
password = os.environ.get("HWE_PASSWORD")

# Kafka topic to produce messages to
topic = 'kafka-connection-test'

# Create Kafka producer
producer = KafkaProducer(security_protocol="SASL_SSL",
                           sasl_mechanism="SCRAM-SHA-512", 
                           sasl_plain_username=username, 
                           sasl_plain_password=password, 
                           bootstrap_servers=bootstrap_servers)

# Define the message to be sent
message = 'Congratulations! You have successfully connected to the HWE Kafka cluster!'

# Produce the message to the topic
producer.send(topic, value=message.encode('utf-8'))

# Define the message to be sent
message = '(You can terminate this program at any time...)'

# Produce the message to the topic
producer.send(topic, value=message.encode('utf-8'))

# Flush the producer to ensure the message is sent
producer.flush()

# Close the producer
producer.close()
