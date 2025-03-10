import socket

# This server only handles one client! There is no multi-threading!
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))  # Bind the server to a local host!

server.listen()

while True:
    client, address = server.accept()
    print(f"Connected to {address}")
    # This parameter which includes (1024 (buffer size)) is more important in UDP, because TCP accepts 1 byte, and stores the others, but UDP will not accept!
    print(client.recv(1024).decode('utf-8'))
    client.send("Hello Client!".encode('utf-8'))
    client.send("Bye!".encode('utf-8'))
    client.close()
