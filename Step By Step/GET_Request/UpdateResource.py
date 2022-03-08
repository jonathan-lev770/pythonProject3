import jsonpath
import requests
import json

# small change to url for put, we add the id at the end

url = "https://reqres.in/api/users/2"

# read input json file
file = open('C:\\Users\\jlevine\\Documents\\Examples file\\CreateUser.json', 'r')  # 'r' is read mode
json_input = file.read()  # as of now, this is a string
request_json = json.loads(json_input)  # changes/parses string into json format
print(request_json)

# make put request with json input body

response = requests.put(url, data=request_json)
print(response.content)
assert response.status_code == 200

# validate response content (so parse it)
response_json = json.loads(response.text)
updatedAt = jsonpath.jsonpath(response_json, 'updatedAt')
print(updatedAt[0])



