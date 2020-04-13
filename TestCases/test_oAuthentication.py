import requests
import json
import jsonpath

def test_oauth_api():
    token_URL = "http://thetestingworldapi.com/Token"
    data = {'grant_type':'password', 'username':'admin', 'password':'adminpass'}
    response = requests.post(token_URL, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')

    auth = {'Authorization':'Bearer' + token_value[0]}

    #Authentication requred URL
    API_URL = "http://thetestingworldapi.com/api/StDetails/164548"
    response = requests.get(API_URL, headers=auth)
    print(response.text)


