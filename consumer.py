from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "room-booking-request",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for bookings in consumer:
    print(f"{bookings.partition}:{bookings.offset} x={bookings.value}")