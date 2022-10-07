"""
pip install confluent-kafka
pip install requests
pip install pandas
pip install jsonschema

"""
import argparse
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer,SerializationContext,MessageField
from confluent_kafka.schema_registry.json_schema import JSONSerializer


"""
# Required connection configs for Kafka producer, consumer, and admin
bootstrap.servers='pkc-xrnwx.asia-south2.gcp.confluent.cloud:9092'
security.protocol=SASL_SSL
sasl.mechanisms=PLAIN
sasl.username={{ CLUSTER_API_KEY }}
sasl.password={{ CLUSTER_API_SECRET }}

# Best practice for higher availability in librdkafka clients prior to 1.7
session.timeout.ms=45000

# Required connection configs for Confluent Cloud Schema Registry
schema.registry.url=https://psrc-epkz2.ap-southeast-2.aws.confluent.cloud
basic.auth.credentials.source=USER_INFO
basic.auth.user.info={{ SR_API_KEY }}:{{ SR_API_SECRET }}
"""

API_KEY = '27WQGWAC6TBWFNE3'
API_SECRET_KEY = 'Y3HdTc7yV04llSz3/X7s+UjaeDQzfAc932f+PEowGFPyiLsMfsJ4oyEbH+C+rnxb'
BOOTSTRAP_SERVER = 'pkc-xrnwx.asia-south2.gcp.confluent.cloud:9092'
SECURITY_PROTOCOL = 'SASL_SSL'
SSL_MECHANISM = 'PLAIN'
ENDPOINT_SCHEMA_URL  = 'https://psrc-epkz2.ap-southeast-2.aws.confluent.cloud'
SCHEMA_REGISTRY_API_KEY = 'MCZML6DBIIRTEUHF'
SCHEMA_REGISTRY_API_SECRET = 'Cbu0kmrG8bvcyOcDaI7YY8PIOu+9AEnVtu96+vOC+/O02vRnzVzGcFvGkiawPv5Z'


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MECHANISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    return sasl_conf


def schema_config():
    return {'url': ENDPOINT_SCHEMA_URL,
            'basic.auth.user.info': f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"
            }

def main(topic):
    producer = Producer(sasl_conf())
    print(producer)

main("restaurant-take-away-data")