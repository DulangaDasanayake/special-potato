import socket
import threading

# Client setup
HOST = '127.0.0.1'
PORT = 5000

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            print("Disconnected from server.")
            break

def send_messages(sock):
    while True:
        msg = input("You: ")
        sock.send(msg.encode())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Start threads for sending and receiving
threading.Thread(target=receive_messages, args=(client,)).start()
threading.Thread(target=send_messages, args=(client,)).start()