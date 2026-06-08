import pytest

# @pytest.mark.skip(reason="Skipped for testing skip")
def test_assertion2():
    assert 1+1 == 2,"false"

a = "jaggu"
b = "jaggu"

@pytest.mark.smoke
def test_assertion4():
    assert a.__eq__(b)

x = "jaggu"
y = "jaggu"
@pytest.mark.xfail(reason="Failed for a testing reason")
def test_assertion5():
    assert x.__eq__(y)

@pytest.mark.parametrize("input,expected",[(1,3),(2,4),(1,3)])
@pytest.mark.sample
def test_assertion6(input,expected):
    assert input + 2 == expected


