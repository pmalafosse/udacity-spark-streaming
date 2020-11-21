from kafka import KafkaConsumer
import json
import time

def run_consumer():
    consumer = KafkaConsumer(
        "com.udacity.sf-crime.police.calls",
        bootstrap_servers=["localhost:9092"],
        client_id="kafka-consumer-calls",
        group_id="0",
        auto_offset_reset="earliest"
    )
    for message in consumer:
        print(message.value)

if __name__ == "__main__":
    run_consumer()
