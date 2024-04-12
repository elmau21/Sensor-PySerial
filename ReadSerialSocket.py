import serial
import csv
import socket
from datetime import datetime

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
        
        # Open CSV file for logging Arduino data
        logging = open('DataArduino.csv', mode='a')
        writer = csv.writer(logging, delimiter=",", escapechar=' ', quoting=csv.QUOTE_NONE)
        
        # Open serial connection to Arduino
        ser = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
        ser.flushInput()
        ser.write(bytes('x', 'utf-8'))  # Send start signal to Arduino
        
        # Receive data from Arduino and send to client
        while True:
            # Read data from Arduino
            ser_bytes = ser.readline()
            decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
            current_time = datetime.now().strftime('%H:%M:%S')
            
            # If Arduino sends "stop", break the loop
            if decoded_bytes == "stop":
                break
            
            # Write received data to CSV file
            writer.writerow([current_time, decoded_bytes])
            
            # Send received data to client
            connection.sendall(decoded_bytes.encode())
        
        # Close connections and files
        ser.close()
        logging.close()
        connection.close()
        print("Logging finished")
        

if __name__ == "__main__":
    HOST = ''  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
    start_server(HOST, PORT)
