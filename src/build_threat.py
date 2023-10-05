import json
import pandas as pd
import yaml
from yaml_operation import *

def save_yaml_content(file_path, content, testing=False):
    if testing:
        print(f"Testing {file_path}: {content}")
        return
    with open(file_path, "w+", encoding="utf-8") as yaml_file:
        yaml.safe_dump(content, yaml_file, encoding='utf-8', allow_unicode=True, default_flow_style=False, sort_keys=False)


def main(threat_directory):
    """main"""
    actor_info = {}
    threat_yaml_files = find_yaml_files(threat_directory)

    print(threat_yaml_files)

    if not threat_yaml_files:
        print("No YAML files found in the specified directory.")
        return

    with open('spec/threat.spec.json', 'r', encoding="utf-8") as stream:
        spec = json.load(stream)
        required = [requirement_field['name'] for requirement_field in spec['requirement']]

    for index, path in enumerate(threat_yaml_files):
        raw = get_yaml_content(path)
        required_contents = {k:raw[k] for k in required if k in raw}
        actor_info[index] = {
            "Index": index,
            **required_contents
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