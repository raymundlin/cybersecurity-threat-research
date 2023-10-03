from src.build_domain import count_yaml_keys as domain_count_yaml_keys
def test_count_yaml_keys():
    assert domain_count_yaml_keys('tests/test_yaml/domain_test1.yaml') == 6
    assert domain_count_yaml_keys('tests/test_yaml/domain_test2.yaml') == 6
    assert domain_count_yaml_keys('tests/test_yaml/domain_test3.yaml') == 6
