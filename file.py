import os
def get_files(folder_name):
    files = []
    for root, dirs, file_names in os.walk(folder_name):
        for file_name in file_names:
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                files.append(os.path.join(root, file_name))
    return files

directory_path = ['domain' , 'threat']

for folder in directory_path:
    yaml_files = get_files(folder)
    print(yaml_files)
