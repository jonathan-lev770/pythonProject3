import requests



response = requests.get("https://api.github.com/")
print(response.status_code)
print(response.raise_for_status())

print('-------------------------------------------------------------------')

response = requests.get("http://api.open-notify.org/astros.json")
print(response)
print(response.content)
print(response.text)
print(response.json())

print('-------------------------------------------------------------------')

query = {'lat': '45', 'lon': '180'}
response = requests.get("http://api.open-notify.org/astros.json", params=query)
print(response.json())

if response.status_code == 200:
    print("Hooray")
else:
    print("boo")

response = requests.post('https://httpbin.org/post', data={'key': 'value'})
requests.put('https://httpbin.org/put', data={'key': 'value'})
print(response.headers["date"])
