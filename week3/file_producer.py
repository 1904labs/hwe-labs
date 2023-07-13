from kafka import KafkaProducer
import gzip

# Kafka broker details
bootstrap_servers = "b-2-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196,b-1-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196,b-3-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196"
kafka_topic = "timsagona"
username = "1904labs"
password= "1904labs"


# Kafka topic to produce messages to
topic = 'timsagona'
limit=5000

# Create Kafka producer
producer = KafkaProducer(security_protocol="SASL_SSL",
                           sasl_mechanism="SCRAM-SHA-512", 
                           sasl_plain_username=username, 
                           sasl_plain_password=password, 
                           bootstrap_servers=bootstrap_servers)

# Read the file
with gzip.open('week2/reviews.tsv.gz', 'rt', encoding='utf-8') as file:
    num_records_sent=0
    # Read each line and send it as a message to Kafka
    for line in file:
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

