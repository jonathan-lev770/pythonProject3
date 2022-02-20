import requests

# get all headers
# response = requests.get('https://httpbin.org/get')
# print(response.text)

# add customized header
# pass the header data in the get request

headerData = {'T1': 'First_Header', 'T2': 'Second_Header'}
response = requests.get('https://httpbin.org/get', headers=headerData)
print(response.text)