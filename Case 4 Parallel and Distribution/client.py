import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter IP: ")
    port = int(input("Enter Port: "))
    client_socket.connect((host, port))

    while True:
        message = input("Enter: ")
        if not message:
            break
        client_socket.sendall(message.encode("utf-8"))

        response = client_socket.recv(1024).decode("utf-8")
        print(response)
    client_socket.close()

if __name__ == "__main__":
    start_client()
