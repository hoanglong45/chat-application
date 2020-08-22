import socket
import threading

username = input("Choose your username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'username':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break


def send():
    while True:
        message = '{}: {}'.format(username, input(''))
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
