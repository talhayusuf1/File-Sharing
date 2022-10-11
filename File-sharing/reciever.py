import os
import socket
import time

host = input("Enter Host Name: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, 22222))
    print("Connected Succesfuly")
except:
    print("Unable to Connect")
    exit(0)

file_name = sock.recv(100).decode()
file_size = sock.recv(100).decode()


with open("./rec/" + file_name, "wb") as file:
    c = 0

    start_time = time.time()

    while c <= int(file_size):
        data = sock.recv(1024)
        if not (data):
            break
        file.write(data)
        c += len(data)

    end_time = time.time()

print("Fİle transfer complite. Total time: ", end_time - start_time)

sock.close()
