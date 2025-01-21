import requests

url = "http://127.0.0.1:5000/api/get"

data = {
    "id": 5,
}

response = requests.get(url, params=data)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")