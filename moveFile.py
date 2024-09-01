import shutil
import os

def move_file(source_path, destination_folder):
    try:
        # Check if the source file exists
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source file not found: {source_path}")

# Ensure the destination folder exists
        if not os.path.isdir(destination_folder):
            raise NotADirectoryError(f"Destination is not a directory: {destination_folder}")

        # Move the file
        shutil.move(source_path, destination_folder)
        print(f"File moved successfully to {destination_folder}")

    except FileNotFoundError as e:
        print(e)
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
