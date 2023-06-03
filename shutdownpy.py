import socket
import os
import pyttsx3


HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

while True:
    communication_socket, address = server.accept()
    message = communication_socket.recv(1024).decode('utf-8')
    if message == "ShutDown Please!":
        sec = 30
        communication_socket.send(f'Ok Mr Badr The Pc will Shutdown in {sec} sec!.'.encode('utf-8'))
        communication_socket.close()
        os.system(f'shutdown /s /t {sec}')
        pyttsx3.speak(f'Ok sir Badr I am shutting down your pc in next {sec} seconds')
    elif message == "Sleep Please!":
        communication_socket.send(f'Ok Mr Badr The Pc will Sleep Now!.'.encode('utf-8'))
        communication_socket.close()
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else:
        communication_socket.close()