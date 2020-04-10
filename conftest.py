import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoading():
    print("User profile data is being created")
    return ["Prasenjit", "Naike", "Nepanagar.com"]

@pytest.fixture(params=[("chrome","PNG","Sonu"), ("Firefox","Naike"),"IE"])
def crossBrowser(request):
    return request.param