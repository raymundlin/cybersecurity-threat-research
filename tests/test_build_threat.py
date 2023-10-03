import os
import sys
sys.path.insert(0, os.path.abspath('..'))
# from src.build_threat import count_yaml_keys,get_yaml_content
from src import build_threat

testPath = "./fakeFolder/apple.com.yaml"

def test_count_yaml_keys():
    num = build_threat.count_yaml_keys(testPath)
    print(num)

def test_get_yaml_content():
    dict = build_threat.get_yaml_content(testPath)
    print(dict)