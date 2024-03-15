from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

producer.send("room-booking-request", value={
    "name": "Ravi",
    "hotel": "Radison",
    "durationOfStay": 7,
    "fromDate": "15-03-2024",
    "toDate": "21-03-2024"
})

