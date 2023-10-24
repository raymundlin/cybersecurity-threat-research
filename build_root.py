import os
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG, filename='rootLog.log')

def get_files(folder_name):
    if folder_name is None:
        logging.fatal('Can not find directory')
    files = []
    for root, dirs, file_names in os.walk(folder_name):
        for file_name in file_names:
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                files.append(file_name)
    return files
    if files is None:
        logging.error('No yaml file in directory')

def get_contents():
    directory_path = ['domain/study' , 'threat/actor']
    topic_files = {dp: get_files(dp) for dp in directory_path}
    contents = []
    for t in topic_files:
        contents.append({'Topic': t, 'Files': '\n'.join(topic_files[t])})
    return contents


with open(f"./README.md", "w+", encoding="utf-8") as markdownFile:
    logging.info('Write content')
    markdownFile.write("### Contents\n")
    markdownFile.writelines(pd.DataFrame(get_contents()).to_markdown(index=False))
