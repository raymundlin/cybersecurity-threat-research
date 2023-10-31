import os
import json
import logging
import emoji
import random

logging.basicConfig(filename = "mylist.jog" , level = logging.DEBUG)
emojis_list = list(emoji.EMOJI_DATA.keys())


def get_files(folder_name):
    """Get all files in a folder recursively."""
    files = []
    for root, dirs, file_names in os.walk(folder_name):
        for file_name in file_names:
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                random_emoji = random.choice(emojis_list)
                files.append(file_name + random_emoji)
                logging.info("Emoji is good to use right ?")
    return files

def main(event, lambda_context):
    """Main function."""
    files = {}
    folders = ["threat/actor", "domain/study"]
    for folder in folders:
        for file in get_files(folder):
            if folder not in files:
                files[folder] = []
            files[folder].append(file)


    return {
        'statusCode': 200,
        'body': json.dumps({
            "data": files,
        })
    }