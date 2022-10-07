import argparse
from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext,MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer

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