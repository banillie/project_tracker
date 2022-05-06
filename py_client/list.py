import requests
from getpass import getpass
import json

auth_endpoint ="http://localhost:8000/api/auth/"
username = input("What is your user name?\n")
password = getpass("What is your password?\n")
# password = getpass()

auth_response = requests.post(auth_endpoint, json={
    'username': username,
    'password': password,
})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint ="http://localhost:8000/api/projects/"

    get_response = requests.get(endpoint, headers=headers)

    # save_path = "api.json"
    # with open(save_path, "w") as write_file:
    #     json.dump(get_response.json(), write_file)

    print(get_response.json())