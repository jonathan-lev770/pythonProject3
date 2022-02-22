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
    response = requests.post(api_url, data=json_request)
    print(response.text)
