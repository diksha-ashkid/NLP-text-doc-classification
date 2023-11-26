import os
import shutil
import logging

# Setting up logging

#use all this in a class
class Move:
    def __init__(self):
        logging.basicConfig(filename='classification.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Function to classify and move files
    def classify_document(self, file_path, class_label):
        # Define your class labels and corresponding folder paths
        class_folders = {
            'News': "D:/Backup/Desktop/programs/NLP-text-doc-classification/demo/news",
            'Research paper': "D:/Backup/Desktop/programs/NLP-text-doc-classification/demo/research",
            'Code': "D:/Backup/Desktop/programs/NLP-text-doc-classification/demo/code",
            'Legal': "D:/Backup/Desktop/programs/NLP-text-doc-classification/demo/legal",
            'Financial Documents': "D:/Backup/Desktop/programs/NLP-text-doc-classification/demo/financial",
            'Medical': "D:/Backup/Desktop/programs/NLP-text-doc-classification/demo/medical",
            # Add more classes and folder paths as needed
        }
        
        # Check if the class label exists
        if class_label in class_folders:
            destination_folder = class_folders[class_label]
            
            # Move the file to the corresponding folder
            try:
                shutil.move(file_path, destination_folder)
                print("here")
                logging.info(f"Moved file {file_path} to {destination_folder}")
            except Exception as e:
                logging.error(f"Error moving file {file_path}: {e}")
        else:
            logging.warning(f"Class label {class_label} not found.")

# Example usage:
file_to_classify = "D:/Backup/Desktop/programs/NLP-text-doc-classification/demo/ex.txt"
assigned_class = 'News'

#classify_document(file_to_classify, assigned_class)

#example 
ex = Move()
ex.classify_document(file_to_classify, assigned_class)