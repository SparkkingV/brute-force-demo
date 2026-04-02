import time

crt_uname = "admin"
crt_pass = "admin"

attempts = 0
delay = 0.1

print("=== CYSEC BRUTE FORCE TOOL ===\n")

with open ("adm_list.txt","r") as admlist:
    for uname in admlist:
         usrname = uname.strip()

         with open("pwd_list.txt" , "r") as file:
            for line in file:
                password = line.strip()
                attempts += 1
                time.sleep(delay)

                print(f"\n [{attempts}] Trying -> {usrname} : {password}")

                if password == crt_pass and usrname == crt_uname:
                    print(f"\n[+] password found! \n")
                    print(f"Attempts : {attempts}")
                    print(f"username : {usrname}")
                    print(f"password : {password}\n")
                    exit()

print(f"\nAttack Failed! credientials not found\n ")
