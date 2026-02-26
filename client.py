import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(ADDR) # try connecting to server
except:
    print("couldn't connect, server may be closed") # if its closed, throw this
    quit()

print(f"CONNECTED TO SERVER AT {ADDR}")

input("UPLOAD / DOWNLOAD / OVERRIDE")


file = open("test.txt", "r")
data = file.read()

client.send("recieved_test.txt".encode(FORMAT)) # sends name
msg = client.recv(SIZE).decode(FORMAT) # receives ACK
print(f"SERVER: {msg}")

client.send(data.encode(FORMAT)) # sends file
msg = client.recv(SIZE).decode(FORMAT) # has to update the msg param

print(f"[SERVER]: {msg}")

file.close()
client.close()
