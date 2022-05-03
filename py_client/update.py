import requests


endpoint = "http://localhost:8000/api/projects/56/update/"

data = {
    "id": 56,
    "name": "Admin isn't great",
    "type": "Project",
    "tier": None,
    "abbreviation": "AIG",
    "scope": None,
    "my_slug": "sluggy_admin-is-great",
    "slug": "admin-is-great",
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
