import os

from get_schema import extract_schema 
from checkSchema import check_schema
from moveFile import move_file
from sendFile import send_file
from sendDF import send_data_as_df

def sendnArchive(filename, bs_file_path, file_path, dest_file_path, bs_archive_folder, archive_folder, producer):
    # print(extract_schema(file_path),filename)
    schema_check = check_schema(filename,extract_schema(file_path))
    # print(schema_check)
    if schema_check == False:
        print(f"got bad schema for{bs_file_path}")
        if os.path.exists(bs_file_path):
            print(f"File {bs_file_path} already exists and will be replaced in bs.")
            os.replace(file_path, dest_file_path)
            print(f"File overwritten successfully to {dest_file_path}")
            
        else:
            print(f"File {bs_file_path} does not exists in bs.")
            move_file(file_path, bs_archive_folder)
            print(f"File {bs_file_path} has been moved to bs.")
        
    else:
        if os.path.isfile(file_path):
            if os.getenv('TRANSFER_MODE') == 'FILE':
                send_file(file_path, producer) 
            if os.getenv('TRANSFER_MODE') == 'DF':
                send_data_as_df(file_path, producer, filename)
        if os.path.exists(dest_file_path):
            print(f"File {dest_file_path} already exists and will be replaced.")
            os.replace(file_path, dest_file_path)
            print(f"File overwritten successfully to {dest_file_path}")

        else:
            print(f"File {dest_file_path} does not exists.")
            move_file(file_path, archive_folder)
            print(f"File {dest_file_path} has been moved.")
        