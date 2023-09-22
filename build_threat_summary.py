""" This py build threat content summary(the number of 'notable incidents' and 'sources of intelligence') md from yaml files """

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


def main(threat_actor_directory):
    """main"""
    actor_content_data = {}
    yaml_files = find_yaml_files(threat_actor_directory)

    print(yaml_files)

    
    if not yaml_files:
        print("No YAML files found in the specified directory.")
        return


    for index, yaml_file_path in yaml_files:
        actor_content = get_yaml_content(yaml_file_path)
        actor_content_data[index] = {
            "Index": index,
            **actor_content,
        }
        del actor_content_data["background"]
        del actor_content_data["attribution"]

    rows = []
    for key, value in actor_content_data.items():
        row = {"Index": key}
        for actor_content_item in value:
            if(actor_content_item == "notable incidents" or "sources of intelligence"):
                value[actor_content_item]=value[actor_content_item].count("-",0)
        row.update(value)
        rows.append(row)

    df = pd.DataFrame(rows)

    # Write Summary
    with open("./thread_summary.md", "w+", encoding="utf-8") as markdownFile:
        markdownFile.write("### Threat 202309\n")
        markdownFile.write("\n")
        markdownFile.writelines(df.to_markdown(index=False))


if __name__ == "__main__":
    main("./threat/actor")
