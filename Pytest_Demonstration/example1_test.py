def test_sample1():
    print("This is sample test 1")

def demo_sample2():
    print("This is sample test 2")

def test_sample3():
    print("This is sample test 3")

def test_assertion1():
    assert 1+1 == 2,"false"

def test_assertion2():
    assert 1+2 == 3,"false"

x = 10
y = 20
def test_assertion3():
    assert x < y,"it is not equal"

a = "jaggu"
b = "jaggu"

def test_assertion4():
    assert a.__eq__(b)