""" This py build summary md from yaml files """

import os
import logging

import pandas as pd
import yaml
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def count_yaml_keys(file_path):
    """count"""
    logging.info('running count_yaml_keys ')
    try:
        with open(file_path, "r", encoding="utf-8") as yaml_file:
            data = yaml.safe_load(yaml_file)
            if data is None:
                logging.warning('file is empty')
                return 0
            return len(data.keys())
    except:
        logging.fatal('Something wrong when open the file path. Please check')


def get_yaml_content(file_path):
    logging.info('running get_yaml_content ')
    try:
        with open(file_path, "r", encoding="utf-8") as yaml_file:
            return yaml.safe_load(yaml_file)
    except IOError as e:
        logging.fatal(e)


def find_yaml_files(root_dir):
    """process all yamls"""
    logging.info('running find_yaml_files ')
    yaml_files = []
    for item in os.listdir(root_dir):
        if os.path.isfile(os.path.join(root_dir, item)):
            if item.endswith(".yaml") or item.endswith(".yml"):
                try :
                    yaml_files.append(os.path.join(root_dir, item))
                except TypeError as e:
                    logging.error(e)
    return yaml_files


def main(root_directory):
    """main"""
    vector = {}
    yaml_files = find_yaml_files(root_directory)

    logging.debug(yaml_files)

    if not yaml_files:
        logging.debug("No YAML files found in the specified directory.")
        return

    for yaml_file_path in yaml_files:
        domain = yaml_file_path.replace("./", "").split("/")[-1]
        if domain.endswith(".yaml"):
            domain = domain[:-6]
        elif domain.endswith(".yml"):
            domain = domain[:-5]
        contents = get_yaml_content(yaml_file_path)
        vector[domain] = {
            "Domain": domain,
            **contents,
        }

    rows = []
    for key, value in vector.items():
        row = {"Domain": key}
        row.update(value)
        rows.append(row)

    df = pd.DataFrame(rows)

    # Write Domain Summary
    try:
        with open(f"{root_directory}/README.md", "w+", encoding="utf-8") as markdownFile:
            markdownFile.write("### domain\Study\n")
            markdownFile.write("\n")
            markdownFile.writelines(df.to_markdown(index=False))
        logging.debug(df)
    except IOError as e:
        logging.fatal(e)

if __name__ == "__main__":
    main("./domain/study")