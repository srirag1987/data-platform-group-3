import socket

# Server address and port
HOST = "localhost"  # Use the service name defined in docker-compose
PORT = 9999

# Open a socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Read the text file in chunks (adjust chunk size as needed)
CHUNK_SIZE = 1024
with open("demo.txt", "rb") as f:
    while True:
        data = f.read(CHUNK_SIZE)
        if not data:
            break
        sock.sendall(data)

print("Data sent successfully!")
sock.close()
