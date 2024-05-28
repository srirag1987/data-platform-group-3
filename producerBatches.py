from faker import Faker
from kafka import KafkaProducer
import json
from time import sleep

# Erstellen des Producers mit Batch-Konfiguration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8'),
    linger_ms=100,
    batch_size=16384
)

# Create a Faker instance
fake = Faker()

# Senden von Nachrichten, die in Batches gesammelt werden
for i in range(50):
    # Generate random data
    name = fake.name()
    email = fake.email()

    # Construct message with random data
    message = {'number': i, 'name': name, 'email': email}

    # Send message
    producer.send('device-data', value=message)
    print(f"Queued: {message}")
    sleep(0.1)  # Optional delay between messages (adjust as needed)

producer.flush()
print("All messages sent.")
