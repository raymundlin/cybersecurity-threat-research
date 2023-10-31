import os
import json
import logging
logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)
def get_files(folder_name):
    """Get all files in a folder recursively."""
    if not folder_name :
        logger.fatal('No folder passed in get_files')
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
        logger.info('start getting file in {}'.format(folder))
        for file in get_files(folder):
            if folder not in files:
                files[folder] = []
            files[folder].append(file)
            logger.debug('Adding {} to list'.format(file))

    logger.info('returning data')
    return {
        'statusCode': 200,
        'body': json.dumps({
            "data": files,
        })
    }