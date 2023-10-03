import sys
sys.path.append("/workspaces/cybersecurity-threat-research/src")

from build_domain import *

yaml_files = find_yaml_files("/workspaces/cybersecurity-threat-research/domain/study")


def test_find_yaml_files():
    assert find_yaml_files("/workspaces/cybersecurity-threat-research/domain/study") is not None

def test_count_yaml_keys():
    for yaml_file_path in yaml_files:
        assert count_yaml_keys(yaml_file_path) != 0

def test_get_yaml_content():
    for yaml_file_path in yaml_files:
        assert get_yaml_content(yaml_file_path) is not None

