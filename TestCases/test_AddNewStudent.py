import requests
import json
import jsonpath

def test_add_student_data():

    API_URL = "http://thetestingworldapi.com/api/studentsDetails"

    file = open('../Test_Data/PostUser.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    print("test for test_add_student_data - " + response.text)

def test_update_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/164130"

    file = open('../Test_Data/PutRequest.json', 'r')
    json_request = json.loads(file.read())
    response = requests.put(API_URL, json_request)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/164130"
    response = requests.get(API_URL)
    # print("test for test_get_student_data - " + response.text)

    #Either way will working file
    # json_response = json.loads(response.text)
    json_response = response.json()
    print(json_response)

    id = jsonpath.jsonpath(json_response, 'data.id')
    # print(id)
    assert id[0] == 164130

def test_delete_student():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/164130"
    response = requests.delete(API_URL)
    print(response.text)
