import socket

HOST ='192.168.8.101'
PORT = 9090
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((HOST,PORT))

socket.send("ShutDown Please!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))