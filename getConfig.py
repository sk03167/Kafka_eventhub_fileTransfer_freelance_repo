import os


def load_kafka_conf(param):
    options = {
        'producer': {
            'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
            'security.protocol': os.getenv('KAFKA_SECURITY_PROTOCOL'),
            'sasl.mechanism': os.getenv('KAFKA_SASL_MECHANISM'),
            'sasl.username': os.getenv('KAFKA_SASL_USERNAME'),
            'sasl.password': os.getenv('KAFKA_SASL_PASSWORD'),
            'sasl.mechanism': os.getenv()
        },
        'consumer': {
            'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),  # Replace with your Kafka broker address
            'security.protocol': os.getenv('KAFKA_SECURITY_PROTOCOL'),
            'sasl.mechanism': os.getenv('KAFKA_SASL_MECHANISM'),  # Replace with your SASL mechanism (e.g., PLAIN, SCRAM-SHA-256, SCRAM-SHA-512)
            'sasl.username': os.getenv('KAFKA_SASL_USERNAME'),  # Replace with your SASL username
            'sasl.password': os.getenv('KAFKA_SASL_PASSWORD'), 
            'group.id': os.getenv('KAFKA_GROUP_ID'),  # Replace with your consumer group
            'auto.offset.reset': os.getenv('KAFKA_AUTO_OFFSET_RESET') # Start reading at the beginning if no previous offset is found
        }
    }
    if param in options:
        # print(options[param])
        return options[param]
    else:
        raise ValueError("Invalid parameter value. Expected 'producer' or 'consumer'.")