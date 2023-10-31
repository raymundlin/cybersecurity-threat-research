import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)

def get_files(folder_name):
    """Get all files in a folder recursively."""
    files = []
    try:
        for root, dirs, file_names in os.walk(folder_name):
            for file_name in file_names:
                if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                    files.append(file_name)
    except IOError as e:
        logger.warning(e)
        logger.debug(e)
    return files

def main(event, lambda_context):
    """Main function."""
    files = {}
    logger.info(f"{event} is starting.")
    folders = ["threat/actor", "domain/study"]
    try:
        for folder in folders:
            for file in get_files(folder):
                if folder not in files:
                    files[folder] = []
                files[folder].append(file)
    except IOError as e:
        logger.fatal(e)
        logger.debug(e)
    logger.info(f"{event} is ending.")
    return {
        'statusCode': 200,
        'body': json.dumps({
            "data": files,
        })
    }