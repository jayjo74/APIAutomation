import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get('https://github.com/login', auth=HTTPBasicAuth('jayjo74', 'sons0310'))
    print(response.text)