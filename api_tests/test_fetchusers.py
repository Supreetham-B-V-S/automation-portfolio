import requests

def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    assert response.status_code == 200

    users = response.json()

    assert len(users) == 10


