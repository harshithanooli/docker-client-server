import os
import hashlib
import socket
import random
import string
import itertools
import sys
    
def generate_random_text_file(file_path, size_of_file):
    characters = string.ascii_letters+string.digits+string.punctuation+string.whitespace
    some_text=''.join(random.choice(characters) for _ in range(size_of_file))
    
    with open(file_path, 'w') as file:
        file.write(some_text)

def main():

    file_path = '/serverdata/random_text_file.txt'
    generate_random_text_file(file_path, 1024)
    with open(file_path, 'rb') as file:
        file_data = file.read()
        checksum = hashlib.sha256(file_data).hexdigest()

    port = 5555
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))  
    server_socket.listen(5)

    for _ in itertools.count():
        client_obj, client_address = server_socket.accept()
        print('Now connected to the address : ', client_address)

        file_size = os.path.getsize(file_path)
        client_obj.send(str(file_size).encode())
        with open(file_path, 'rb') as file:
            client_obj.sendfile(file)

        client_obj.send(checksum.encode())
        client_obj.close()

if __name__ == "__main__":
    main()