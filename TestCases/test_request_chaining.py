import requests
import json
import jsonpath

def test_add_new_student():
    global id  #id variable will be global
    # 1. Add New Student
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('../Test_Data/AddUser.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(API_URL, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

def test_get_details():
    # 2. Get Details of last added student
    Detail_URL = "http://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(Detail_URL)
    print(response.text)

