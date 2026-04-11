import socket
import threading

def receive():
    while True:
        msg = conn.recv(1024).decode()
        print(f"\nClient: {msg}")

host = "0.0.0.0"
port = 5000

server = socket.socket()
server.bind((host, 5000))
server.listen(1)

print("[WAITING FOR CONNECTION...]")
conn, addr = server.accept()
print(f"[CONNECTED] {addr}")

threading.Thread(target=receive).start()

while True:
    msg = input("You: sdfgg")
    conn.send(msg.encode())