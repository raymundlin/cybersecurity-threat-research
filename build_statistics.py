""" This py build threat content summary(the number of 'notable incidents' and 'sources of intelligence') md from yaml files """

import os

import pandas as pd
import yaml
import logging

logging.basicConfig(filename='build_statistics.log', encoding='utf-8', level=logging.DEBUG)

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
        logging.warn("You need pass parameter in find_yaml_files func.")
    yaml_files = []
    for item in os.listdir(root_dir):
        if os.path.isfile(os.path.join(root_dir, item)):
            if item.endswith(".yaml") or item.endswith(".yml"):
                yaml_files.append(os.path.join(root_dir, item))
    return yaml_files


def main(main_dir, main_key, len_keys=[]):
    """main"""
    main_content_data = {}
    yaml_files = find_yaml_files(main_dir)

    logging.debug(yaml_files)


    if not yaml_files:
        logging.fatal("No YAML files found in the specified directory.")
        return

    for index, yaml_file_path in enumerate(yaml_files):
        raw_content = get_yaml_content(yaml_file_path)
        main_content = {}
        if main_key:
            main_content["name"] = raw_content["threat actor"]
        else:
            dms = yaml_file_path.split("/")[-1].split(".")
            del dms[-1]
            main_content["name"] = '.'.join(dms)
        main_content["keys"] = list(raw_content.keys())
        main_content["nkeys"] = len(raw_content.keys())
        for k in len_keys:
            main_content[k] = len(raw_content[k])
        main_content_data[index] = {
            "Index": index,
            **main_content,
        }

    rows = []
    for key, value in main_content_data.items():
        row = {"Index": key}
        row.update(value)
        rows.append(row)

    df = pd.DataFrame(rows)

    # Write Summary
    parts = main_dir.split("/")
    title = parts[1] + " " + parts[2]
    parts[-1] = "README.md"
    with open("/".join(parts), "w+", encoding="utf-8") as markdownFile:
        logging.info("Start Generate Statistics Table...")
        markdownFile.write(f"### {title} 202309\n")
        markdownFile.write("\n")
        markdownFile.writelines(df.to_markdown(index=False))


if __name__ == "__main__":
    logging.info("=== Statistics Builder Start ===")
    main("./threat/actor", "threat actor", ["notable incidents", "sources of intelligence"])
    main("./domain/study", None, [])
    logging.info("=== Statistics Builder Finish ===")
