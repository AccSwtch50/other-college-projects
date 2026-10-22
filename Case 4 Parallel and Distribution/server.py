import time,socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server is listening on {host} at port {port}...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Server connected to client {client_address}")

            while True:
                message = client_socket.recv(1024).decode("utf-8")
                if not message:
                    client_socket.close()
                    break
                print(f"Client message: {message}")

                client_socket.sendall(f"Echo: {message}".encode("utf-8"))

    except KeyboardInterrupt:
        server_socket.close()

if __name__ == "__main__":
    start_server("127.0.0.1", 65342)
