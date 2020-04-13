import requests
import json
import jsonpath

def test_Add_new_data():

    # 1. Add New Student
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('../Test_Data/PostUser.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(API_URL, request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    # 2. Add Technical Skills
    addSkill_URL = "http://thetestingworldapi.com/api/technicalskills"
    file = open('../Test_Data/TechnicalSkill.json', 'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(addSkill_URL, request_json)
    print(response.text)

    # # 3. Add Address
    addAddress_URL = "http://thetestingworldapi.com/api/addresses"
    file = open('../Test_Data/Address.json', 'r')
    request_json = json.loads(file.read())
    request_json['stId'] = id[0]
    response2 = requests.post(addAddress_URL, request_json)
    print(response2.text)

    # 4. Fetch Complete details - Final Student Details
    finalDetail_URL = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response3 = requests.get(finalDetail_URL)
    print(response3.text)




