import requests

TYPE_CHOICES = [
    ("Project", "PROJECT"),
    ("Programme", "PROGRAMME"),
    ("Portfolio", "PORTFOLIO"),
]


# endpoint = "https://httpbin.org/anything"
endpoint ="http://localhost:8000/api/"
# endpoint = "https://httpbin.org/status/200/"


get_response = requests.post(endpoint, json={
    "name": 'api project 4',
    "type": 'Project',
    "abbreviation": 'apip 4',
    })  # HTTPs request

# print(get_response.text)
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notion ~ Python Dict
print(get_response.json())
# print(get_response.status_code)
