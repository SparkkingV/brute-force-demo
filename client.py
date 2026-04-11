import socket
import threading

def receive():
    while True:
        msg = client.recv(1024).decode()
        print(f"\nServer: {msg}")

target_ip = "10.24.172.32"  # CHANGE THIS
port = 5000

client = socket.socket()
client.connect((target_ip, port))

print("[CONNECTED]")

threading.Thread(target=receive).start()

while True:
    msg = input("You: ")
    client.send(msg.encode())