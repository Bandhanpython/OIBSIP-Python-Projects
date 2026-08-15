import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("Connected to server!")
print("You can start chatting.")


def receive_messages():
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            print("\nFriend:", message.decode())

        except:
            break  


thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()


while True:
    message = input("You: ")

    if message.lower() == "exit":
        break

    client.send(message.encode())


client.close()  