import requests

endpoint ="http://localhost:8000/api/projects/"

data = {
    "name": "teleology",
    "type": "Project",
    "abbreviation": "TELE",
}
get_response = requests.post(endpoint, json=data)

print(get_response.json())