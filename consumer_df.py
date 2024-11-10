import pandas as pd
import os
from confluent_kafka import Producer, KafkaError, Consumer
import json
import pickle

from dotenv import load_dotenv
load_dotenv('/Users/shivanshk/Documents/pdev/kafapp1/config.env')


from getConfig import load_kafka_conf


consumer = Consumer(load_kafka_conf('consumer_local'))

# topic_name = "kafkahub"

topic = os.getenv('KAFKA_TOPIC_LOCAL')

output_path = "/Users/shivanshk/Documents/pdev/kafapp1/test_recieve_folder"

def get_filename(filename):
    if not '.csv' in filename:
        filename = f"{filename.split(".")[0]}.csv"
    return filename

def consume_data_df():
    consumer.subscribe([topic])
    print("called df conusme data",topic)
    while True:
        msg = consumer.poll(1.0)
        print("Polling for data")
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
        else:
            data = pickle.loads(msg.value())
            print(msg)
            df = data['df']
            filename = get_filename(data['filename'])
            batch_number = data['batch_number']

            print(f"batch number:{batch_number}  filename: {filename}")

            if not os.path.isdir(output_path):
                os.makedirs(output_path)
                print(f"CREATED {output_path}")
            
            key = msg.key().decode("utf-8")
            if key == "0":
                df.to_csv(f"{output_path}/{filename}", index=False, mode="a", header=True)
            else:
                df.to_csv(f"{output_path}/{filename}", index=False, mode="a", header=False)


# if __name__ == "__main__":
#     def consume_data_df():
# ()
