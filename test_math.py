from math_utils import square_number

def test_square_number():
    assert square_number(4) == 16
    assert square_number(-2) == 4
    assert square_number(0) == 0