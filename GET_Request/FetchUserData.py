import requests
import json
import jsonpath

# API URL (parameters are part of the URL), GET request

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print(response)

# display response content
# display response headers

print(response.content)
print(response.headers)

# validate status code

print(response.status_code)
assert response.status_code == 200

# this time, fetch specific content of response headers

print(response.headers.get("Date"))
print(response.headers.get("Server"))

# fetch cookies from the response
print(response.cookies)

# fetch Encoding
print(response.encoding)

# fetch elapse time (time between request sent and request received
print(response.elapsed)

print('----------------------------------------------------------------------------------------')

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print(response.content)

# Parse response to json format

json_response = json.loads(response.text)
print(json_response)

# Fetch value using json path
# when we apply jsonpath to any response, it will return a list

pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])  # this will be 2 as per the url page
assert pages[0] == 2  # simple assert

# fetch the first first_name

first_first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(first_first_name[0])
assert first_first_name == ["Michael"]


#  fetch all the first names

for i in range(0, 3):  # range will ignore 3, so index 0, 1, 2
    first_names = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
    print(first_names)

# so the range is index 0, 1, 2
# we can't hard code the index like if we want 1 specific name, so we need to pass 'i'
# but in python, we can't concatenate numeric value with string, so we wrap it in str class


