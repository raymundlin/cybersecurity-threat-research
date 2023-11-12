import os
import pandas as pd
import logging
from flagsmith import Flagsmith

logging.basicConfig(filename='build_root.log', encoding='utf-8', level=logging.DEBUG)

flagsmith = Flagsmith(
    environment_key='ser.UQk4uU3ZMNYcQwsreizvc6',
    # os.environ['FLAGSMITH_KEY'],
    enable_local_evaluation=True)
flagsmith.update_environment()
flags = flagsmith.get_environment_flags()
traits = {}
if os.environ.get('BOT'):
    traits['bot'] = True

segs = flagsmith.get_identity_segments(identifier="undefined", traits=traits)
print(segs)


def get_files(folder_name):
    files = []
    if not folder_name:
        logging.warn("You need pass parameter in get_files func.")
    for root, dirs, file_names in os.walk(folder_name):
        for file_name in file_names:
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                files.append(file_name)
                logging.debug("find file: {} in folder({})".format(file_name, folder_name))
    return files


def get_contents():
    directory_path = []
    if flags.is_feature_enabled('domain_info'):
        directory_path.append('domain/study')
    if flags.is_feature_enabled('threat_info'):
        directory_path.append('threat/actor')
    topic_files = {dp: get_files(dp) for dp in directory_path}
    contents = []
    for t in topic_files:
        contents.append({'Topic': t, 'Files': '\n'.join(topic_files[t])})
    return contents


with open(f"./README.md", "w+", encoding="utf-8") as markdownFile:
    logging.info("=== Root Builder Start ===")
    markdownFile.write("### Contents\n")
    markdownFile.writelines(pd.DataFrame(get_contents()).to_markdown(index=False))
    logging.info("=== Root Builder Finished ===")
