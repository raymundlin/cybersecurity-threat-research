"""Module providing test functions for src.yaml_operation."""
import os
from src.yaml_operation import *


os.chdir("./")

def test_count_yaml_keys():
    """test keys' number"""
    assert count_yaml_keys('tests/test_yaml/domain_test1.yaml') == 6
    assert count_yaml_keys('tests/test_yaml/domain_test2.yaml') == 6
    assert count_yaml_keys('tests/test_yaml/domain_test3.yaml') == 6

def test_find_yaml_files():
    """test files' number and type"""
    files = find_yaml_files("tests/test_yaml")
    # test number of files
    assert len(files) == 3
    # test file type
    for file in files:
        assert file.endswith(".yaml") or file.endswith('yml')

def test_get_yaml_content():
    """test file's key and value"""
    yaml_test1 = get_yaml_content('tests/test_yaml/domain_test1.yaml')
    # test key
    assert 'dig' in yaml_test1
    assert 'whoisrws' in yaml_test1
    assert 'dnsdumpster' in yaml_test1
    assert 'shodan' in yaml_test1
    assert 'censys' in yaml_test1
    assert 'nmap' in yaml_test1
    #test value
    assert yaml_test1['dig'] == 'apple.com relays to 17.253.144.10\n'
    assert yaml_test1.get('whoisrws').startswith('Name: APPLE.COM')
    assert yaml_test1.get('whoisrws').endswith('URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/\n')
    assert yaml_test1.get('dnsdumpster').startswith('TXT record')
    assert yaml_test1.get('dnsdumpster').endswith('"Dynatrace-site-verification=7d881a7c-c13f-4146-9d27-2731459e2509__iqls0105tagglcsaul0m16ibrf"\n')
    assert yaml_test1.get('shodan').startswith('ports: 80, 443')
    assert yaml_test1.get('shodan').endswith('Content-Length: 287\n')
    assert yaml_test1.get('censys').startswith('Basic Information')
    assert yaml_test1.get('censys').endswith('Protocols: 80/HTTP , 443/HTTP\n')
    assert yaml_test1.get('nmap').startswith('Nmap scan report for apple.com (17.253.144.10)')
    assert yaml_test1.get('nmap').endswith('443/tcp open  https\n')


