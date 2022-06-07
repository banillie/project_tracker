import requests


# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(
    endpoint,
    json={'data': 'hello world'}
)
# print(get_response.text)
print(get_response.json())

