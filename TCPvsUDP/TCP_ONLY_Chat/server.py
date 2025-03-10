#Simple TCP Chat Room in Python
import threading
import socket

host = '127.0.0.1'  # Local host
#choose ports which are not reserved , reserved : 80 , 443
port = 5555  # Port number 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #type of socket!
server.bind((host, port))  # Bind needs a tuple
server.listen()  # Start listening for incoming connections

#make 2 empty lists, so when adding a new client fisrt : add it to the client list then get the nick name of it and add it to nick name list.
clients = []
nicknames = []

# Broadcast function to send messages to all clients connected to the server
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle messages from clients
def handle(client):
    while True:
        try:
            # Try to receive a message from the client
            message = client.recv(1024)
            broadcast(message)
        except:
            # If an error occurs, remove the client
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

# Receive clients
def receive():
    while True:
        # Accept all connections and return client and address
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        # Get nickname of client
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        
        print(f'Nickname of the client is: {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
