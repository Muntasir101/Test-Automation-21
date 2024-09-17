import pytest


@pytest.fixture
def BrowserConfigure():
    print("Browser Launch")


@pytest.fixture
def UrlConfig():
    print("URL open")


@pytest.fixture
def CompleteConfigure():
    print("Browser Launch")
    print("URL open")