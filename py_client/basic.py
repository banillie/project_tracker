import requests

# endpoint = "https://httpbin.org/anything"
endpoint ="http://localhost:8000/api/"
# endpoint = "https://httpbin.org/status/200/"


get_response = requests.get(
    endpoint,
    params={"abc": 123},
    json={"query": "Hello World"}
    )  # HTTPs request

# print(get_response.text)
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notion ~ Python Dict
print(get_response.json())
# print(get_response.status_code)
