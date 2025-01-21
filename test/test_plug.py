import requests

url = "http://127.0.0.1:5000/api/plug"
data = {
    "id": 1,
}

for i in range(1, 50):
    data["id"] = i
    response = requests.post(url, json=data)

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")