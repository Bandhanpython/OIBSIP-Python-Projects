import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

print("Server started...")
print("Waiting for clients...")

clients = []


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            print("Message:", message.decode())
            broadcast(message, client)

        except:
            break

    if client in clients:
        clients.remove(client)

    client.close()


while True:
    client, address = server.accept()

    print("Connected:", address)

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()  