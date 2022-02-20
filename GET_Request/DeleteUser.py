import requests

# delete the user with id 2

url = "https://reqres.in/api/users/2"
response = requests.delete(url)
print(response.status_code)
assert response.status_code == 204