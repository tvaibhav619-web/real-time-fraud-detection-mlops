from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    txn = {
        "user_id": random.randint(1, 10000),
        "amount": round(random.uniform(10, 9000), 2),
        "merchant_risk": random.uniform(0, 1),
        "transaction_hour": random.randint(0, 23)
    }
    producer.send("transactions", txn)
    time.sleep(1)
