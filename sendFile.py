
import os
import json
import base64

def send_file(file_path,producer):

    topic = os.getenv('KAFKA_TOPIC')
    chunk_size = eval(os.getenv('CHUNK_SIZE'))

    with open(file_path, 'rb') as file:
        filename = os.path.basename(file_path)
        chunk_number = 0
        while chunk := file.read(chunk_size):
            print("reading chunk number ", chunk_number)
            message = {
                'filename': filename,
                'chunk_number': chunk_number,
                'total_chunks': (os.path.getsize(file_path) + chunk_size - 1) // chunk_size,
                'data': base64.b64encode(chunk).decode('utf-8')
            }
            # print(topic, type(message['data']),message['data'])
            producer.produce(topic, key=str(chunk_number), value=json.dumps(message))
            producer.flush()
            chunk_number += 1