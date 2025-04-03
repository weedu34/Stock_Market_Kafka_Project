import pandas as pd
from kafka import  KafkaProducer
from time import sleep
from json import dumps
import json
print("All libraries imported")

producer = KafkaProducer(bootstrap_servers = ['13.53.42.38:9092'],
                         value_serializer = lambda x:dumps(x).encode('utf-8'))
producer.send('demo_testing', value="{'Hello': 'World'}")