""" This py build summary md from yaml files """
import os
import pandas as pd
import yaml
import logging

logging.basicConfig(filename='build_domain.log', encoding='utf-8', level=logging.DEBUG)
logging.info("Start")
logging.warning("You have to make sure there is at least one yaml or yml file")


def count_yaml_keys(file_path):
    """count"""
@@ -35,6 +38,8 @@ def find_yaml_files(root_dir):
        if os.path.isfile(os.path.join(root_dir, item)):
            if item.endswith(".yaml") or item.endswith(".yml"):
                yaml_files.append(os.path.join(root_dir, item))
            else:
                logging.error("There's no yaml or yml file.")
    return yaml_files