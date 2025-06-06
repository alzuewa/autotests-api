import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = 'localhost', 12345
client_socket.connect(server_address)

message = 'Hi, server!'
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f'Response from server: {response}')

client_socket.close()
