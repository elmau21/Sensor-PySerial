import ping3
import time

arduino_ip = '192.168.1.177'  # Replace with the real Arduino's IP address

def ping_arduino():
    while True:
        response_time = ping3.ping(arduino_ip)
        if response_time is not None:
            print(f"Arduino is reachable. Response time: {response_time} ms")
        else:
            print("Arduino is unreachable.")
        time.sleep(5)  # Ping every 5 seconds

if __name__ == "__main__":
    ping_arduino()
