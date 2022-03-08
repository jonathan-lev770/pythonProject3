import jsonpath
import requests
import json
import pytest

url = "https://reqres.in/api/users"


#  the purpose of this class was just to show that we can create multiple test cases starting with test
#  and the file itself starts wtih test  (we deleted a lot of stuff from the code here)

@pytest.fixture(scope="module")
def start_exec():
    global file
    file = open('C:\\Users\\jlevine\\Documents\\Examples file\\CreateUser.json', 'r')  # 'r' is read mode


@pytest.mark.Smoke
def test_create_user(start_exec):
    # read input json file
    json_input = file.read()  # as of now, this is a string
    request_json = json.loads(json_input)  # changes/parses string into json format
    response = requests.post(url, data=request_json)
    assert response.status_code == 201


@pytest.mark.Sanity
def test_create_other_user(start_exec):
    # read input json file
    file = open('C:\\Users\\jlevine\\Documents\\Examples file\\CreateUser.json', 'r')  # 'r' is read mode
    json_input = file.read()  # as of now, this is a string
    request_json = json.loads(json_input)  # changes/parses string into json format
    response = requests.post(url, data=request_json)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])  # it will always return a list, so you  say print first element
