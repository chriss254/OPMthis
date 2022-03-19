from backend.event_generation.create_csv_file import create_csv_file
from backend.event_generation.kafka_consumer import NewKafkaConsumer
from backend.event_generation.kafka_listener import kafka_listener


class CsvLogGenerator:

    def __init__(self):

        create_csv_file()

        kafka_consumer = NewKafkaConsumer('schlaegerbande_events', 'localhost:9092').consumer

        kafka_listener(kafka_consumer)








