import request(method, url, body=None, headers={})

url = "http://127.0.0.1:1106"

with open("passwords.txt", "r") as file:
    for line in file:
        data = {"username": username,
                "password": password
                    }