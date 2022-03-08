import pytest
import requests
import json
import jsonpath


@pytest.mark.Smoke
def test_fetch_user_details():
    # API URL (parameters are part of the URL), GET request
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    json_response = json.loads(response.text)
    #  fetch all the first names
    for i in range(0, 3):  # range will ignore 3, so index 0, 1, 2
        first_names = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
        print(first_names)

    # so the range is index 0, 1, 2
    # we can't hard code the index like if we want 1 specific name, so we need to pass 'i'
    # but in python, we can't concatenate numeric value with string, so we wrap it in str class
