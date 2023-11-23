import os
import shutil
import logging

# Setting up logging
logging.basicConfig(filename='classification.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to classify and move files
def classify_document(file_path, class_label):
    # Define your class labels and corresponding folder paths
    class_folders = {
        'class1': '/path/to/class1/folder',
        'class2': '/path/to/class2/folder',
        # Add more classes and folder paths as needed
    }
    
    # Check if the class label exists
    if class_label in class_folders:
        destination_folder = class_folders[class_label]
        
        # Move the file to the corresponding folder
        try:
            shutil.move(file_path, destination_folder)
            logging.info(f"Moved file {file_path} to {destination_folder}")
        except Exception as e:
            logging.error(f"Error moving file {file_path}: {e}")
    else:
        logging.warning(f"Class label {class_label} not found.")

# Example usage:
file_to_classify = '/path/to/your/document.txt'
assigned_class = 'class1'

classify_document(file_to_classify, assigned_class)