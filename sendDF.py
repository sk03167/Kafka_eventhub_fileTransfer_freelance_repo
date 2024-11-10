import pandas as pd
import pickle
import os

def check_format_and_read(file_path: str, filename: str, schema_file_path: str):
    df = None
    valid_schema = False
    # correct_file_format = "valid file format"
    
    if ".csv" in filename:
        print(f"Found CSV file: {filename}")
        df = pd.read_csv(file_path)
        # valid_schema = validate_schema(df, schema_file_path)
    elif ".json" in filename:
        print(f"Found Json file: {filename}")
        df = pd.read_json(file_path)
        # valid_schema = validate_schema(df, schema_file_path)
    elif ".xlsx" in filename:
        print(f"Found excel file: {filename}")
        df = pd.read_excel(file_path)
        # valid_schema = validate_schema(df, schema_file_path)
    elif ".parquet" in filename:
        print(f"Found parquet file: {filename}")
        df = pd.read_parquet(file_path)
        # valid_schema = validate_schema(df, schema_file_path)
    elif ".orc" in filename:
        print(f"Found orc file: {filename}")
        df = pd.read_orc(file_path)
        # valid_schema = validate_schema(df, schema_file_path)
    # else:
    #     correct_file_format = "invalid file format"

    return df

def get_batches(df):
    batch_size = 5
    batches = [df[i : i + batch_size] for i in range(0, len(df), batch_size)]
    print()
    return batches


def delivery_callback(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(
            f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}"
        )


def send_data_as_df(filepath, producer, filename):
    df = check_format_and_read(filepath, filename, None)
    batch_cnt = 0
    batches = get_batches(df)
    for batch in batches:
        message = {
            "batch_number": batch_cnt,
            "df": batch,
            "filename": filename
        }
        data = pickle.dumps(message)
        producer.produce(os.getenv('KAFKA_TOPIC_LOCAL'), key=f"{batch_cnt}", value=data, callback=delivery_callback)
        producer.flush()
        batch_cnt += 1
    