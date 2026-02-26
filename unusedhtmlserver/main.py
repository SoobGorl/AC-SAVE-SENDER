import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP = SOCK_STREAM, DGRAM = UDP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.setblocking(False)

server_socket.bind((SERVER_HOST, SERVER_PORT)) # 127.0.0.0 is only this computer, 0.0.0.0 is EVERYONE

server_socket.listen(5) # 5 = number of maximum of fully established connections that can wait in queue


print(f"Listening on port {SERVER_PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    # print(f"{client_socket}, {client_address}")
    request = client_socket.recv(1024).decode()
    print(request)
    headers = request.split("\n")
    first_header_components = headers[0].split()

    http_method = first_header_components[0]
    path = first_header_components[1]

    if http_method == "GET":
        if path == '/':
            fin = open("index.html")
            content = fin.read()
            fin.close()

            response = "HTTP/1.1 200 OK\n\n" + content
            client_socket.sendall(response.encode())
            client_socket.close()
    else:
        response = "HTTP/1.1 405 Method Not Allowed\n\nAllow: GET"