import os
import json
import logging 

logging.basicConfig(filename = 'clc.log', level=logging.DEBUG)


def get_files(folder_name):
    """Get all files in a folder recursively."""
    files = []
    for root, dirs, file_names in os.walk(folder_name):
        for file_name in file_names:
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                files.append(file_name)
            else: logging.error("Your extention need to be .yaml or .yml")
    return files

def main(event, lambda_context):
    """Main function."""
    logging.info("start!")
    files = {}
    folders = ["threat/actor", "domain/study"]
    for folder in folders:
        for file in get_files(folder):
            if folder not in files:
                files[folder] = []
                logging.debug("Your file can't be null")
            files[folder].append(file)
    logging.info("Ending!") 
    return {
        'statusCode': 200,
        'body': json.dumps({
            "data": files,
        })
    
    }