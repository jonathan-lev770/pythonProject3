import pytest

# Test Case code must be written inside a method
# Method name must start with test


@pytest.fixture(scope="module")
def fixture_code():
    print("This is our fixture code will execute before test case")
    print("-------------------------------------------------------")
    yield
    print("Close db connection after executing test case")
    print("-------------------------------------------------------")



@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc001_login_logout_testing(fixture_code):
    print("This is smoke test case")
    print("This is end of my test case")


@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc003_login_logout_invalid_credentials(fixture_code):
    print("This is sanity test case")
    print("This is end of test case")

# print statement output display on console:  -s
# verbose mode - display test cases name with status (pass or file):   -v
