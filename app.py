from flask import Flask, request
from kafka import KafkaProducer
from kafka.vendor import six
from datetime import datetime
import json

app = Flask(__name__)
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)


@app.route("/bookings", methods=['POST'])
def create_bookings():
    booking = request.get_json()
    booking["created_at"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    producer.send("room-booking-request", booking)
    return booking


if __name__ == '__main__':
    app.run()
