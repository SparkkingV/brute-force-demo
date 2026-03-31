crt_pass = "123_admin"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("enter password : ")

    import time
    time.sleep(1)

    if password == crt_pass:
        print(f"Access Granted..!")
        break
    else:
        attempts += 1
        print(f"Wrong Password!")

    if attempts == max_attempts:
        print(f"!Account locked due to many failed attempts")
