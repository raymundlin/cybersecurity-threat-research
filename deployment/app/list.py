import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_files(folder_name):
    """Get all files in a folder recursively."""
    if folder_name is None:
        logger.error("No dictionary")
        logger.debug("File not found")
    files = []
    for root, dirs, file_names in os.walk(folder_name):
        for file_name in file_names:
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                files.append(file_name)
    return files
def main(event, lambda_context):
    """Main function."""
    files = {}
    folders = ["threat/actor", "domain/study"]
    for folder in folders:
        for file in get_files(folder):
            if folder not in files:
                files[folder] = []
                logger.fatal("File not found")
                logger.debug("File not found")
            files[folder].append(file)

    return {
        'statusCode': 200,
        'body': json.dumps({
            "data": files,
        })
    }