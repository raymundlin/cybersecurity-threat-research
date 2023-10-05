""" This py build summary md from yaml files """

import pandas as pd
from yaml_operation import *

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
        row.update(value)
        rows.append(row)

    df = pd.DataFrame(rows)

    # Write Domain Summary
    with open(f"{root_directory}/README.md", "w+", encoding="utf-8") as markdownFile:
        markdownFile.write("### domain\Study\n")
        markdownFile.write("\n")
        markdownFile.writelines(df.to_markdown(index=False))
        print(df)

if __name__ == "__main__":
    main("./domain/study")