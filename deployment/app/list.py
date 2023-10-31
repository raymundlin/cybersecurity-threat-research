import os
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_files(folder_name):
    """Get all files in a folder recursively."""
    files = []
    for root, dirs, file_names in os.walk(folder_name):
        for file_name in file_names:
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                files.append(file_name)
    logger.info('Get files from %s',folder_name)
    return files

def main(event, lambda_context):
    """Main function."""
    logger.info("-Start-")
    files = {}
    folders = ["threat/actor", "domain/study"]
    for folder in folders:
        for file in get_files(folder):
            if folder not in files:
                files[folder] = []
            files[folder].append(file)
    logger.info("Finished getting files")
    logger.info("-End-")
    return {
        'statusCode': 200,
        'body': json.dumps({
            "data": files,
        })
    }
