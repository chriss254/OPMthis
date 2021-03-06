import csv
import json
import re

class KafkaListener ():
    def __init__(self,consumer, config):
        self.consumer = consumer
        self.config = config
    
    def listen(self):
        for msg in self.consumer:
            print("Kafka consumer received message")
            
            # Get actual payload from message and split to work with csv.writer
            event_json = json.loads(msg.value.decode('utf-8'))
            payload =""

            # Build string from message to store in event log
            for attribute in self.config['eventAttributes']:
                if payload != "":
                    payload += ","
                if attribute == "event":
                    # Only take URL ending and cut out the base URL
                    payload += re.search(self.config['baseUrl'] + '(.*)', event_json[attribute]).group(1)
                if attribute != "event":
                    payload += str(event_json[attribute])

            # Append to CSV file
            with open('backend/files/events.csv', 'a', newline='') as csv_dump:
                writer = csv.writer(csv_dump, delimiter=';')
                writer.writerow(payload.split(","))
                print(payload)
        