import os
import shutil
import logging

def organize_files(directory):
    """
    Organizes files in the specified directory into subfolders based on their file extensions.

    Args:
        directory (str): The path to the directory to organize.
    """
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
        "Videos": [".mp4", ".mkv", ".webm", ".flv", ".vob", ".avi", ".wmv", ".mov", ".mpg", ".mpeg", ".3gp"],
        "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
        "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".csv"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    }

    # Create folders for each file type if they don't exist
    for folder in file_types.keys():
        if not os.path.exists(folder):
            os.makedirs(folder)

    files_moved = False

    # Iterate through the files in the directory
    for file in os.listdir(directory):
        if os.path.isfile(file):
            # Getting the file extension
            _, ext = os.path.splitext(file)

            # Check which folder the file belongs to
            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    try:
                        # Move the file to the corresponding folder
                        shutil.move(file, os.path.join(folder, file))
                        print(f"Moved {file} to {folder}/")
                        logging.info(f"Moved {file} to {folder}/")
                        files_moved = True
                    except Exception as e:
                        print(f"Error moving file {file}: {e}")
                        logging.error(f"Error moving file {file}: {e}")
                    break

    if not files_moved:
        print("No files to organize in the specified directory.")
        logging.info("No files to organize in the specified directory.")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(filename='file_organizer.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    # Specify the directory you want to organize
    directory_to_organize = input("Enter the directory you want to organize: ")
    organize_files(directory_to_organize)