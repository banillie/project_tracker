import requests

endpoint ="http://localhost:8000/api/projects/"

data = {
    "name": "wouldn't it be nice",
    "type": "Project",
    "abbreviation": "wibn",
}
get_response = requests.post(endpoint, json=data)

print(get_response.json())