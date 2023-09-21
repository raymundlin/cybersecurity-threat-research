import os

# # 列出所有YAML
folders = ["threat", "domain"]
yaml_files = []
for folder in folders:
    # print(folder)
    for root, dirs, file_names in os.walk(folder):
        for file_name in file_names:
            #print(file_name)
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                yaml_files.append(file_name)

print(yaml_files)


# yaml_files = [file for file in current_file_list if file.endswith('.yaml') or file.endswith('.yml')]

# # print所有 YAML 文件
# for yaml_file in yaml_files:
#     print(yaml_file)
