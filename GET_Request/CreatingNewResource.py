import jsonpath
import requests
import json

url = "https://reqres.in/api/users"

# read input json file
file = open('C:\\Users\\jlevine\\Documents\\Examples file\\CreateUser.json', 'r')  # 'r' is read mode
json_input = file.read()  # as of now, this is a string
request_json = json.loads(json_input)  # changes/parses string into json format
print(request_json)

# make post request with json input body

response = requests.post(url, data=request_json)
print(response.content)
assert response.status_code == 201

# fetch headers from response
# fetch value from a specific header   -- >  remember it's a get to do this

print(response.headers)
print(response.headers.get("Content-Length"))

# fetch id from response
# first response to json format
response_json = json.loads(response.text)

# now you can print the id from json path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])  # it will always return a list, so you  say print first element if you don't want it as a list






