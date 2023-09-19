""" This py build summary md from yaml files in threat/actor dir """

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
    mypath = "threat/actor"
    research_data = {}
    yaml_files = find_yaml_files(mypath)

    print(yaml_files)

    if not yaml_files:
        print("No YAML files found in the specified directory.")
        return

    for yaml_file_path in yaml_files:
        student_id = yaml_file_path.replace("./", "").split(".")[0].upper()
        research = get_yaml_content(yaml_file_path)
        research_data[student_id] = {
            "Student ID": student_id,
            **research,
        }

    rows = []
    for key, value in research_data.items():
        row = {"Student ID": key}
        row.update(value)
        rows.append(row)

    df = pd.DataFrame(rows)

    # Write Score Summary
    with open("./README.md", "w+", encoding="utf-8") as markdownFile:
        markdownFile.write("### Devops202309\n")
        markdownFile.write("Research Summary\n")
        markdownFile.write("\n")
        markdownFile.writelines(df.to_markdown(index=False))


if __name__ == "__main__":
    main("./")
