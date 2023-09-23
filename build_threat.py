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
    with open(file_path,"r", encoding="utf-8") as yaml_file:
        return yaml.safe_load(yaml_file)

def find_yaml_files(root_dir):
    """process all yamls"""
    yaml_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".yaml"):  # or file.endswith(".yml")
                yaml_files.append(os.path.join(root, file))
    return yaml_files

def main(threat_directory):
    """main"""
    actor_info = {}
    threat_yaml_files = find_yaml_files(threat_directory)

    print(threat_yaml_files)

    if not threat_yaml_files:
        print("No YAML files found in the specified directory.")
        return

    for index, path in enumerate(threat_yaml_files):
        actor_info[index] = {
            "Index": index,
            **get_yaml_content(path)
        }

    print(actor_info)

    rows = []
    for key, value in actor_info.items():
        row = {"Index": key}
        row.update(value)
        rows.append(row)

    threat_actor_list = pd.DataFrame(rows)
    print(threat_actor_list)

    with open(f"{threat_directory}/README.md", "w+", encoding="utf-8") as markdownFile:
        markdownFile.write("### Threat Actors\n")
        markdownFile.writelines(threat_actor_list.to_markdown(index=False))

if __name__ == "__main__":
    main("./threat/actor")