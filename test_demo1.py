# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
# You can run specific file with py.test <filename>
# You can mark (Tag) tests @pytest.mark.smoke and then run with -m
# You can skip test with @pytest.mark.skip
# Fixtures are used for setup and tear down methods for test cases- conftest file to generalize
# fixtures and make it available to all test cases
# Datadriven and Parameterization can be done with return statements in tuple format
# When you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_SecodeGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])