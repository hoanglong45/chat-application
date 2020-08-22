import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
users = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            user = users[index]
            broadcast('{} left!'.format(user).encode('utf-8'))
            users.remove(user)
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('username'.encode('utf-8'))
        user = client.recv(1024).decode('utf-8')
        users.append(user)
        clients.append(client)

        print("Username is {}".format(user))
        broadcast("{} joined!".format(user).encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is starting !")
receive()
