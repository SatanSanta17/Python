# the name needs to be as mentioned "test_<filename>" it is mandatory

from calc import square
import pytest

def main():
    test_positive_square()
    test_negative_square()
    test_str_square()

# assert keyword
# pytest library
def test_positive_square():
    assert square(2)==4
    assert square(3)==9
def test_negative_square():
    assert square(-2)==4
def test_str_square():
    with pytest.raises(TypeError):
        square("cat")

if __name__=="__main__":
    main()