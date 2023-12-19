import os
import json
import logging

logging.basicConfig(filename='list.log', level=logging.DEBUG)
logging.info("Start")
logging.warning("You have to make sure there is at least one yaml or yml file")

def get_files(folder_name):
    """Get all files in a folder recursively."""
@@ -8,21 +13,26 @@ def get_files(folder_name):
        for file_name in file_names:
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                files.append(file_name)
            else:
                logging.error("There's no yaml or yml file.")
    return files

def main(event, lambda_context):
    """Main function."""
    logging.debug("Executing Main")
    files = {}
    folders = ["threat/actor", "domain/study"]
    folders = ["threat/actor", "domain/study", "backup"]
    for folder in folders:
        for file in get_files(folder):
            if folder not in files:
                files[folder] = []
            files[folder].append(file)

    logging.info("Finished")

    return {
        'statusCode': 200,
        'body': json.dumps({
            "data": files,
        })
    }
    }