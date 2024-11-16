import socket
import threading

# Server setup
HOST = '127.0.0.1'
PORT = 5000
clients = []

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                print(f"Message received: {msg}")
                broadcast(msg, client_socket)
        except:
            clients.remove(client_socket)
            break

def broadcast(msg, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(msg.encode())

# Start the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"Server started on {HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    print(f"Connection from {addr}")
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()