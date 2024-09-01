import pandas as pd
import csv
import xml.etree.ElementTree as ET
import json
import avro.schema
import pyarrow
import fastparquet

def extract_schema(file_path):
    # print(file_path)
    file_extension = file_path.split('.')[-1]
    # print(file_extension)
    if file_extension in ['csv', 'txt']:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            schema = next(reader)
            return schema

    elif file_extension in ['xml']:
        tree = ET.parse(file_path)
        root = tree.getroot()
        schema = [child.tag for child in root]
        return schema

    elif file_extension in ['json']:
        data = pd.read_json(file_path)
            
            # Print the DataFrame
     
            
            # Get the column names as schema
        schema = list(data.columns)
        print(schema)
            
        return schema

    elif file_extension in ['avro']:
        with open(file_path, 'r') as file:
            schema = avro.schema.parse(file.read())
            schema = schema.fields
            return schema

    elif file_extension in ['parquet', 'orc', 'hdf5']:
        df = pd.read_parquet(file_path) if file_extension == 'parquet' else pd.read_orc(file_path) if file_extension == 'orc' else pd.read_hdf(file_path)
        schema = df.columns.tolist()
        return schema

    else:
        raise ValueError("Unsupported file format")
