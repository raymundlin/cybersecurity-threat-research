""" This py build summary md from yaml files """

import os

import pandas as pd
import yaml

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
    """main"""
    vector = {}
    yaml_files = find_yaml_files(root_directory)

    print(yaml_files)

    if not yaml_files:
        print("No YAML files found in the specified directory.")
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
        for element in value:
            if element != "Domain":
                value[element] = "X"
        row.update(value)
        rows.append(row)

    df = pd.DataFrame(rows)

    # Write Domain Summary
    with open("./README.md", "w+", encoding="utf-8") as markdownFile:
        markdownFile.write("### domain\Study\n")
        markdownFile.write("\n")
        markdownFile.writelines(df.to_markdown(index=False))
        print(df)

if __name__ == "__main__":
    main("./domain/study")