import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users"

#Read Input Json file
file = open('D:\\API\\CreateUser.json', 'r') #Open file with read mode
json_input = file.read()    #Read file
request_json = json.loads(json_input)  #Change json format

#Make POST request with Json Input body
response = requests.post(url, request_json)
# print(response.content)

#Validating Response Code
assert response.status_code == 201

#Fetch Header from Response
print(response.headers.get('Content-Length') + ' - Content Length')

#Parse response to Json Format
response_json = json.loads(response.text)

#Pick ID using Json Path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0] + ' - id value.')