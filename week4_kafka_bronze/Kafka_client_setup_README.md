# Setting up the Kafka command line utilities locally

## Setup

### Setting up a JAAS file
```
KafkaClient {
   org.apache.kafka.common.security.scram.ScramLoginModule required
   username="secretusername"
   password="secretpassword";
};
```

### Download the truststore to your computer
`/home/you/kafka.client.truststore.jks`

### Setting up a SASL properties file @ /home/you/client_sasl.properties
```
security.protocol=SASL_SSL
sasl.mechanism=SCRAM-SHA-512
ssl.truststore.location=/home/you/kafka.client.truststore.jks
enable.idempotence=false
```

### Setting up Kafka CLI environment variables
```
export KAFKA_HEAP_OPTS="-Xms512m -Xmx1g"
export KAFKA_OPTS=-Djava.security.auth.login.config=/home/you/users_jaas.conf
```

## Running the Kafka CLI commands

### List the topics
`kafka-topics.sh --bootstrap-server $HWE_BOOTSTRAP --command-config /home/you/client_sasl.properties --list`

### Create a topic
`kafka-topics.sh --bootstrap-server $HWE_BOOTSTRAP --create --topic TOPIC --command-config /home/you/client_sasl.properties --partitions 1 --replication-factor 3`

### kafka-console-consumer.sh
`kafka-console-consumer.sh --bootstrap-server $HWE_BOOTSTRAP --from-beginning --consumer.config ./client_sasl.properties --topic timsagona`

### kafka-console-producer.sh
`kafka-console-producer.sh --bootstrap-server $HWE_BOOTSTRAP --producer.config ./client_sasl.properties --topic timsagona`