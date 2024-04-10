import socket

def start_server(host, port):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the address
        server_socket.bind((host, port))
        
        # Listen for incoming connections
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")
        
        # Accept incoming connections
        connection, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Receive data from the client
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            
            # Echo the received data back to the client
            connection.sendall(data)
            
        # Close the connection
        connection.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    start_server(HOST, PORT)
