import os
import shutil

def delete_stored_folder_contents(folder_path):
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)  # Delete file
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Delete folder
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
