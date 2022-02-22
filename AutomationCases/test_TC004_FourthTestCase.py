import pytest

# Test Case code must be written inside a method
# Method name must start with test

a = 101


# Decorator
# @pytest.mark.skipif(a > 100, reason="Skipping this test bc this functionality not working, dev will fix in next build")
@pytest.mark.Smoke
def test_tc001_login_logout_testing():
    print("This is smoke test case")
    print("This is end of my test case")


@pytest.mark.Sanity
def test_tc003_login_logout_invalid_credentials():
    print("This is sanity test case")
    print("This is end of test case")

# print statement output display on console:  -s
# verbose mode - display test cases name with status (pass or file):   -v
