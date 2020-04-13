import requests

param = {'name':'jay', 'email':'jay@google.com', 'number':'2938782838'}
url = "https://httpbin.org/get"
response = requests.get(url, params=param)
print(response.text)