import pytest


@pytest.fixture(scope='function', autouse=True)
def hook(request):
    #BEFORE TEST
    print("======================== Before Test ====================")

    yield
    #AFTER TEST
    print("========================= After Test======================")

@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # BEFORE TEST
    print("======================== Before ALL ====================")

    yield
    # AFTER TEST
    print("========================= After ALL =====================")