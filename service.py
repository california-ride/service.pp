#!/usr/bin/python3

import socket
import threading

def handle_client(client_socket):
    response = "Enter Your Name:"
    client_socket.send(response.encode('utf-8'))
    
    name = client_socket.recv(1024).decode('utf-8')
    
    response = "Hello " + name
    client_socket.send(response.encode('utf-8'))
    
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 3434))
    server.listen(5)
    
    print("Server listening on port 3434...")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
