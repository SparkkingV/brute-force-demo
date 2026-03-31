username = "admin"
crt_pass = "123_adm"

attempts = 0


with open("pwd_list.txt" , "r") as file:
    for line in file:
        password = line.strip()
        attempts += 1
        import time
        time.sleep(0.5)

        print(f"\n Trying : {password}")

        if password == crt_pass:
            print(f"\npassword found")
            print(f"Attempts : {attempts}")
            print(f"password : {password}\n")
            break
        else:
            print(f"password not found!")


