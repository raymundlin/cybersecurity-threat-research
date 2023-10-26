""" This py build summary md from yaml files """

import os

import pandas as pd
import yaml

import logging 
from logtrace import LogTrace#pip install logtrace

logger = logging.getLogger('')
trace = LogTrace(logger=logger)

def count_yaml_keys(file_path):
    """count"""
    with open(file_path, "r", encoding="utf-8") as yaml_file:
        data = yaml.safe_load(yaml_file)
        if data is None:
            return 0
        return len(data.keys())


def get_yaml_content(file_path):
    with open(file_path, "r", encoding="utf-8") as yaml_file:
        return yaml.safe_load(yaml_file)


def find_yaml_files(root_dir):
    """process all yamls"""
    yaml_files = []
    for item in os.listdir(root_dir):
        if os.path.isfile(os.path.join(root_dir, item)):
            if item.endswith(".yaml") or item.endswith(".yml"):
                yaml_files.append(os.path.join(root_dir, item))
    return yaml_files


def main(root_directory):
    trace.add("Start")
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='domain/storelog.log',filemode='w', encoding='utf-8', level=logging.INFO)
    """main"""
    vector = {}
    yaml_files = find_yaml_files(root_directory)

    print(yaml_files)
    logging.info('print yaml_files')

    if not yaml_files:
        print("No YAML files found in the specified directory.")
        logging.warning('%s YAML files', 'No')
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
    with open(f"{root_directory}/README.md", "w+", encoding="utf-8") as markdownFile:
        markdownFile.write("### domain\Study\n")
        markdownFile.write("\n")
        markdownFile.writelines(df.to_markdown(index=False))
        logging.info('Already Written Domain Summary')
        print(df)

    trace.add("Finish")
    trace.emit()

if __name__ == "__main__":
    main("./domain/study")
