import socket
from validate_savefile import *

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

print("[STARTING] Server is starting.")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("[LISTENING] Server is listening.")




while True:
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    filename = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Filename received. {filename}")
    file = open(filename, "w")
    #file = open("directory/"+filename, "w")
    conn.send(f"Filename received. {filename}".encode(FORMAT))

    data = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] File data received.")
    file.write(data) # writes the file that was received
    conn.send("File data received.".encode(FORMAT))

    conn.send("Closing connection.".encode(FORMAT))

    file.close() # closes file
    conn.close() # closes communication between client and server
    print(f"[DISCONNECTED] {addr} force disconnected.")