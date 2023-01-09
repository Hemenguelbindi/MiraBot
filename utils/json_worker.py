import json


def add_user_json(id_user: int, user_name: str):
    with open("users.json", "r") as users:
        data_from_json = json.load(users)
    
    user_id = id_user
    username = user_name
    if str(user_id) not in data_from_json:
        data_from_json[user_id] = {"username": username}

    with open("users.json", "w") as add:
        json.dump(data_from_json, add, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    add_user_json(5555, "max")