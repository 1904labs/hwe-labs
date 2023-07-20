from kafka import KafkaProducer

# Kafka broker details
bootstrap_servers = "b-2-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196,b-1-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196,b-3-public.hwekafkacluster.6d7yau.c16.kafka.us-east-1.amazonaws.com:9196"
kafka_topic = "timsagona"
username = "1904labs"
password= "1904labs"


# Kafka topic to produce messages to
topic = 'timsagona'

# Create Kafka producer
producer = KafkaProducer(security_protocol="SASL_SSL",
                           sasl_mechanism="SCRAM-SHA-512", 
                           sasl_plain_username=username, 
                           sasl_plain_password=password, 
                           bootstrap_servers=bootstrap_servers)

# Define the message to be sent
message = 'Hello from Python'

# Produce the message to the topic
producer.send(topic, value=message.encode('utf-8'))

# Flush the producer to ensure the message is sent
producer.flush()

# Close the producer
producer.close()
