import socket
import sqlite3

# Function to handle incoming connections
def handle_connection(connection, client_address):
    print(f"Connection from {client_address}")
    
    # Connect to SQLite database
    db_connection = sqlite3.connect('example.db')
    db_cursor = db_connection.cursor()
    
    try:
        # Receive data from the client
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            
            # Insert data into database
            db_cursor.execute("INSERT INTO messages (message) VALUES (?)", (data.decode(),))
            db_connection.commit()
            
            # Echo the received data back to the client
            connection.sendall(data)
            
    finally:
        # Close the database connection
        db_connection.close()
        # Close the connection with the client
        connection.close()

# Function to fetch all messages from the database
def get_all_messages():
    # Connect to SQLite database
    db_connection = sqlite3.connect('example.db')
    db_cursor = db_connection.cursor()

    try:
        # Retrieve all messages from the database
        db_cursor.execute("SELECT * FROM messages")
        messages = db_cursor.fetchall()
        return messages
    finally:
        # Close the database connection
        db_connection.close()

def start_server(host, port):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the address
        server_socket.bind((host, port))
        
        # Listen for incoming connections
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")
        
        # Accept incoming connections and handle them
        while True:
            connection, client_address = server_socket.accept()
            handle_connection(connection, client_address)
            print("Messages in the database:")
            messages = get_all_messages()
            for message in messages:
                print(message)

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    start_server(HOST, PORT)
