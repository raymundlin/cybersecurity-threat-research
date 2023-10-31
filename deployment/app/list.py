import os
import json
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def get_files(folder_name):
    """Get all files in a folder recursively."""
    if not folder_name :
        logging.fatal('No folder passed in get_files')
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
        logging.info('start getting file in {}'.format(folder))
        for file in get_files(folder):
            if folder not in files:
                files[folder] = []
            files[folder].append(file)
            logging.debug('Adding {} to list'.format(file))

    logging.info('returning data')
    return {
        'statusCode': 200,
        'body': json.dumps({
            "data": files,
        })
    }