import socket

# This server only handles one client! There is no multi-threading!
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # DGRAM is related to UDP!!
server.bind(('127.0.0.1', 5555))  # Bind the server to a local host!

message, address = server.recvfrom(1024)
print(message.decode('utf-8'))
server.sendto("Hello Client!".encode('utf-8'), address)
