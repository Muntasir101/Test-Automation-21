import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_case1_valid(BrowserConfigure, UrlConfig):
    print("Testing Test Case 1 completed.")


@pytest.mark.sanity
@pytest.mark.skip("We don't want to run this test")
def test_case2_invalid(BrowserConfigure, UrlConfig):
    print("Testing Test Case 2 completed.")


@pytest.mark.sanity
def test_case3_invalid(BrowserConfigure, UrlConfig):
    print("Testing Test Case 3 completed.")


@pytest.mark.smoke
def test_case4_valid(BrowserConfigure, UrlConfig):
    print("Testing Test Case 4 completed.")
