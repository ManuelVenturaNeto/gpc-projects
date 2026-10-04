import logging
import time
import json
from google.api_core.exceptions import NotFound
from google.cloud import pubsub_v1
from faker import Faker
from dotenv import load_dotenv
from .config import settings

load_dotenv()

publisher = pubsub_v1.PublisherClient()
topic_name = publisher.topic_path(settings.PROJECT_ID, settings.TOPIC_NAME)

try:
    publisher.get_topic(topic=topic_name)
except NotFound:
    publisher.create_topic(name=topic_name)


sub = pubsub_v1.SubscriberClient()
subscription_name = sub.subscription_path(settings.PROJECT_ID, settings.SUBSCRIPTION)

try:
    sub.get_subscription(subscription=subscription_name)
except NotFound:
    sub.create_subscription(name=subscription_name, topic=topic_name)

def generate_data():
    while True:
        faker = Faker(locale='pt_BR')
        data = {
            'name': faker.name(),
            'age': faker.random_int(min=18, max=66),
            'city': faker.city()
        }
        logging.info(data)

        data = json.dumps(data, ensure_ascii=False).encode('utf-8')

        future = publisher.publish(topic=topic_name, data=data, spam='eggs')
        future.result()    
        
        time.sleep(0.5)

