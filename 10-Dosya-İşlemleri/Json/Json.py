import json

with open("users.json") as users:
    data = json.load(users)
    print(data[0]["username"])
    print(data[0]["email"])
    print(data[0]["address"]["street"])
