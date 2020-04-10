import pytest


def test_firstProgram():
    msg = "Hello"
    assert  msg == "Hi", "Test failed because string don't match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition don't match"


@pytest.fixture()
def setup():
    print("I will be executing first")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")