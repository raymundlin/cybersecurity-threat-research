
from src.module_a import square
def test_square():
    assert square(8) == 64

def test_error ():
    assert square(8) == 64

    if square(8) == 64:
        print("正確")
    else:
        print("錯誤")


