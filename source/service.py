import requests

database = {
    1: "John",
    2: "Mary",
    3: "Bob",
    4: "Jane",
}


def get_user_from_db(user_id):
    return database[user_id]


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError(400, "Bad Request")