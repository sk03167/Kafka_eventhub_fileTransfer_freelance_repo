from confluent_kafka import Consumer
import os
import json
import base64
import pickle
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
    if os.getenv('TRANSFER_MODE') == 'FILE':
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

    if os.getenv('TRANSFER_MODE') == 'DF':
        def get_filename(filename):
            if not '.csv' in filename:
                filename = f"{filename.split(".")[0]}.csv"
            return filename

        def consume_data_df():
            consumer.subscribe([topic])
            print("called df conusme data",topic)
            while True:
                msg = consumer.poll(1.0)
                # print("Polling for data")
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

                    if not os.path.isdir(destination_folder):
                        os.makedirs(destination_folder)
                        print(f"CREATED {destination_folder}")
                    
                    key = msg.key().decode("utf-8")
                    if key == "0":
                        df.to_csv(f"{destination_folder}/{filename}", index=False, mode="a", header=True)
                    else:
                        df.to_csv(f"{destination_folder}/{filename}", index=False, mode="a", header=False)
        consume_data_df()
if __name__ == "__main__":
    main()
