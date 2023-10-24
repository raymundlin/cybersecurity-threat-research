""" This py build summary md from yaml files """

import os

import pandas as pd
import yaml
import logging

logging.basicConfig(filename='build_domain.log', encoding='utf-8', level=logging.DEBUG)

def count_yaml_keys(file_path):
    """count"""
    if not file_path:
        logging.fatal("You need pass parameter in count_yaml_keys func.")
    with open(file_path, "r", encoding="utf-8") as yaml_file:
        data = yaml.safe_load(yaml_file)
        if data is None:
            return 0
        return len(data.keys())


def get_yaml_content(file_path):
    if not file_path:
        logging.fatal("You need pass parameter in get_yaml_content func.")
    with open(file_path, "r", encoding="utf-8") as yaml_file:
        return yaml.safe_load(yaml_file)


def find_yaml_files(root_dir):
    """process all yamls"""
    if not root_dir:
        logging.warning("You need pass parameter in find_yaml_files func.")
    yaml_files = []
    for item in os.listdir(root_dir):
        if os.path.isfile(os.path.join(root_dir, item)):
            if item.endswith(".yaml") or item.endswith(".yml"):
                yaml_files.append(os.path.join(root_dir, item))
    return yaml_files


def main(root_directory):
    """main"""
    logging.info("Start Fetching YAML files...")
    vector = {}
    yaml_files = find_yaml_files(root_directory)

    logging.debug(yaml_files)

    if not yaml_files:
        logging.fatal("No YAML files found in the specified directory.")
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

    logging.info("Finish Fetching YAML files.")

    # Write Domain Summary
    with open(f"{root_directory}/README.md", "w+", encoding="utf-8") as markdownFile:
        logging.info("Start Generate Domains Table...")
        markdownFile.write("### domain\Study\n")
        markdownFile.write("\n")
        markdownFile.writelines(df.to_markdown(index=False))
        logging.debug(df)

if __name__ == "__main__":
    logging.info("=== Domain Builder Start ===")
    main("./domain/study")
    logging.info("=== Bomain Builder Finished ===")