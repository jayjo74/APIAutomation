import requests

#API URL
url = "https://reqres.in/api/users?page=2"

#Send Get request
response = requests.get(url)

#Display Response Content
print(response.content)
print(response.headers)

#Validate Status Code
print(response.status_code)
assert response.status_code == 200

# Fetch Response Header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

#Fetch Cookies
print(response.cookies)

#Fetch Encoding
print(response.encoding)

#Fetch elapse time
print(response.elapsed)



