import os
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 22222))
sock.listen(5)
print("HOST:", sock.getsockname())

client, addr = sock.accept()

file_name = input("File Name:")
file_size = os.path.getsize(file_name)

client.send(file_name.encode())

client.send(str(file_size).encode())

with open(file_name, "rb") as file:
    c = 0

    start_time = time.time()
    while c <= file_size:
        data = file.read(1024)
        if not (data):
            break
        client.sendall(data)
        c += len(data)
    end_time = time.time()

print("File transfer complete. Total time: ", end_time - start_time)

sock.close()
