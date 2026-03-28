username = "admin"
crt_pass = "123_adm"

pass_list =["1234","123admin","admin@123","helloworld","admin","123_adm"]

attempts = 0

for password in pass_list :
    attempts += 1
    print(f"trying : {password}")

    if password == crt_pass:
        print("\n password found!")
        print(f"password : {password}")
        print(f"attempts : {attempts}")
        break
    else:
        print(f"password not found!")
