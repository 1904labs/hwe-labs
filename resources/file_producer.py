import os
from kafka import KafkaProducer
import gzip

# Load environment variables.
from dotenv import load_dotenv
load_dotenv()

# Kafka broker details
bootstrap_servers = os.environ.get("HWE_BOOTSTRAP")
username = os.environ.get("HWE_USERNAME")
password = os.environ.get("HWE_PASSWORD")


# Kafka topic to produce messages to
topic = 'reviews'
limit=5000

# Create Kafka producer
producer = KafkaProducer(security_protocol="SASL_SSL",
                           sasl_mechanism="SCRAM-SHA-512", 
                           sasl_plain_username=username, 
                           sasl_plain_password=password, 
                           bootstrap_servers=bootstrap_servers)

# Read the file
with gzip.open('resources/reviews.tsv.gz', 'rt', encoding='utf-8') as file:
    num_records_sent=0
    # Read each line and send it as a message to Kafka
    for index, line in enumerate(file):
        if index == 0:
            continue #Skip the first line in case it's a header row
        message = line.strip().encode('utf-8')
        producer.send(topic, value=message)
        #print(line)
        num_records_sent+=1
        if num_records_sent % 1000 == 0:
            print(f"Records sent: {num_records_sent}")
        if num_records_sent == limit:
            break

# Flush the producer to ensure the message is sent
producer.flush()

# Close the producer
producer.close()

