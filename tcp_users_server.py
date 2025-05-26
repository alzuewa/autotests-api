import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = 'localhost', 12345
    server_socket.bind(server_address)

    server_socket.listen(10)

    message_history = []

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'User with address: {client_address} connected to server')

        client_message = client_socket.recv(1024).decode()
        message_history.append(client_message)
        print(f'User with address: {client_address} sent a message: {client_message}')

        client_socket.send('\n'.join(message_history).encode())

        client_socket.close()


if __name__ == '__main__':
    server()
