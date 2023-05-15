import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('localhost', 8000))

# Listen for incoming connections
server_socket.listen(1)

print('Server started')

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print('Connected by', client_address)

    # Handle the connection
    data = client_socket.recv(1024)
    client_socket.sendall(data)

    # Close the connection
    client_socket.close()