import requests
import json
import jsonpath


# to post using this method
# create a file to post in notebook++
# create variable to load the file as json by passing file.read()
# make your api call (post) passing the url, and the data=, save it in response file

def test_add_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\jlevine\\Documents\\Examples file\\RequestJson.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(api_url, json_request)
    print(response.text)


#if you run this again, make sure to change the assert
def test_get_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/1024156"
    response = requests.get(api_url)
    json_response = response.json()
    # json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'data.id')  # remember it always returns a list
    assert id[0] == 1024156  # assert [0] so result is not a list


# this test doesn't work but it should
def test_update_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/1024156"
    file = open('C:\\Users\\jlevine\\Documents\\Examples file\\RequestJson_Update.json', 'r')
    json_request = json.loads(file.read())
    response = requests.put(api_url, json_request)
    print(response.text)


def test_delete_student():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/1024156"
    response = requests.delete(api_url)
    print(response.text)
