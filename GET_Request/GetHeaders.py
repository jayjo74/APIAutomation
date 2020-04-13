import requests

headerdata = {'t1':'First_Header', 't2':'Second_Header'}
url = "https://httpbin.org/get"
response = requests.get(url, headers=headerdata)
print(response.text)