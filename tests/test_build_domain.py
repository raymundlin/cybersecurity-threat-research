import sys
sys.path.append("./")

import build_domain
import build_statistics
import build_threat

PATH = "./domain/study"
PATH2 = "./threat/actor"

yaml_files = build_domain.find_yaml_files(PATH)
yaml_files2 = build_threat.find_yaml_files(PATH2)
yaml_files3 = build_statistics.find_yaml_files(PATH)

def test_count_yaml_keys():
    for yaml_file_path in yaml_files:
        assert build_domain.count_yaml_keys(yaml_file_path) != 0

    for yaml_file_path in yaml_files2:
        assert build_threat.count_yaml_keys(yaml_file_path)

def test_get_yaml_content():
    for yaml_file_path in yaml_files:
        assert build_domain.get_yaml_content(yaml_file_path) is not None
        assert build_statistics.get_yaml_content(yaml_file_path) is not None

    for yaml_file_path in yaml_files2:
        assert build_threat.get_yaml_content(yaml_file_path) is not None