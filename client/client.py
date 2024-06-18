import os
import hashlib
import socket
import sys
import itertools

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 5555
    if len(sys.argv)>1:
        port = int(sys.argv[1])

    client_socket.connect(("server", port))
    file_size = int(client_socket.recv(1024).decode())
    received_server_data = b""
    for _ in itertools.count():
        while len(received_server_data) < file_size:
            received_chunk = client_socket.recv(min(file_size - len(received_server_data), 1024))
            if not received_chunk:
                break
            received_server_data += received_chunk

        checksum = client_socket.recv(64).decode()
        received_client_checksum = hashlib.sha256(received_server_data).hexdigest()
        if checksum == received_client_checksum:
            print("Verified checksum, it is matched, check for the file in client shell!")

            with open('/clientdata/received_file_from_server.txt', 'wb') as f:
                f.write(received_server_data)
        sys.stdout.flush()

if __name__ == "__main__":
    main()