import sys
sys.path.append("./")

import build_domain

PATH = "./tests/test"

def test_yaml_files():
    assert build_domain.find_yaml_files(PATH) is not None
