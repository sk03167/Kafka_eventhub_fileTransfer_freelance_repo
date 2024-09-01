from confluent_kafka import Producer
import os

import shutil
from dotenv import load_dotenv
load_dotenv('/Users/shivanshk/Documents/pdev/kafapp1/config.env')


from getConfig import load_kafka_conf

from sendnArchive import sendnArchive


# print (load_kafka_conf('producer'))

producer = Producer(load_kafka_conf('producer'))
# topic = 'filetransferhub'
# chunk_size = 1024 * 500  # 1 MB


if __name__ == "__main__":
    source_folder = '/Users/shivanshk/Documents/pdev/kafapp1/test_folder'
    archive_folder = '/Users/shivanshk/Documents/pdev/kafapp1/archive'
    bs_archive_folder = '/Users/shivanshk/Documents/pdev/kafapp1/archive/bs'
    
    while len(os.listdir(source_folder)):
        print(os.listdir(source_folder))
        if len(os.listdir(source_folder)) ==1 and os.listdir(source_folder)[0] == '.DS_Store':
            break
        for filename in os.listdir(source_folder):
            if filename == '.DS_Store':
                continue
            
            file_path = os.path.join(source_folder, filename)
            dest_file_path = os.path.join(archive_folder, filename)
            bs_file_path = os.path.join(bs_archive_folder,filename)

            sendnArchive(filename, bs_file_path, file_path, dest_file_path, bs_archive_folder, archive_folder,producer)