import os
import json
import logging

logging.basicConfig(filename = 'myapp.log', level = logging.INFO)

def get_files(folder_name):
    """Get all files in a folder recursively."""
    files = []
    for root, dirs, file_names in os.walk(folder_name):
        for file_name in file_names:
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                files.append(file_name)
            else: 
                logging.error(f"{file_name} not include .yaml or .yml")
                logging.debug(f"{file_name} not include .yaml or .yml")
    
    return files

def main(event, lambda_context):
    """Main function."""
    logging.info("Start")
    files = {}
    folders = ["threat/actor", "domain/study"]
    try:
        for folder in folders:
            for file in get_files(folder):
                if folder not in files:
                    files[folder] = []
                files[folder].append(file)
    except IOError as e:
        logging.fatal(e)
        logging.debug(e)

    logging.info("End")
    return {
        'statusCode': 200,
        'body': json.dumps({
            "data": files,
        })
    }