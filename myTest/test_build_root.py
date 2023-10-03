from build_root import get_files

def test_getFiles():
    assert type(get_files('/domain/study')) == list