import sys
sys.path.append("./")

from build_domain import *

PATH = "./domain/study"

yaml_files = find_yaml_files(PATH)


def test_find_yaml_files():
    assert find_yaml_files(PATH) is not None

def test_count_yaml_keys():
    for yaml_file_path in yaml_files:
        assert count_yaml_keys(yaml_file_path) != 0

def test_get_yaml_content():
    for yaml_file_path in yaml_files:
        assert get_yaml_content(yaml_file_path) is not None