from confluent_kafka import Consumer
import os
import json
import base64
from dotenv import load_dotenv
load_dotenv('/Users/shivanshk/Documents/pdev/kafapp1/config.env')


from getConfig import load_kafka_conf

consumer = Consumer(load_kafka_conf('consumer_local'))
topic = os.getenv('KAFKA_TOPIC_LOCAL')
consumer.subscribe([topic])

destination_folder = '/Users/shivanshk/Documents/pdev/kafapp1/test_recieve_folder'

def save_chunk(filename, chunk_number, data):
    with open(os.path.join(destination_folder, filename), 'ab') as file:
        file.write(data)

def main():
    file_parts = {}
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print(msg.error())
            continue

        message = json.loads(msg.value().decode('utf-8'))
        filename = message['filename']
        chunk_number = message['chunk_number']
        total_chunks = message['total_chunks']
        data = base64.b64decode(message['data'])
        
        # Initialize the file_parts dictionary if necessary
        if filename not in file_parts:
            file_parts[filename] = {'total_chunks': total_chunks, 'received_chunks': set()}

        # Save the chunk
        save_chunk(filename, chunk_number, data)
        file_parts[filename]['received_chunks'].add(chunk_number)

        # Check if all chunks are received
        if len(file_parts[filename]['received_chunks']) == total_chunks:
            print(f"File {filename} received and reconstructed.")
            print(file_parts[filename]['received_chunks'],total_chunks)

if __name__ == "__main__":
    main()
