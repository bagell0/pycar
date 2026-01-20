import socket

HOST = "0.0.0.0"
PORT = 5000

print("Starting receiver...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a TCP IPv4 socket

s.bind((HOST, PORT))

s.listen(1) #one client at a time

print("Waiting for connection")

conn, addr = s.accept() #waits until another computer connects

print("Connected from", addr)

while True:
    data = conn.recv(1024) #waits for data reads up to 1024 bytes
    if not data:
        break
    print("RECEIVED:", data.decode("utf-8", errors="replace"))


conn.close() #closes connection
s.close() #releases port


