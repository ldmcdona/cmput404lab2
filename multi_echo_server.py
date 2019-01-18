#!/usr/bin/env python3
import socket
from multiprocessing import Process
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #Question 3, socket option, so_reuseaddr
        #Question 4, it prints: connected by: client IP , port
        #Question 5, It returns None
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("Started process ", p)

def handle_echo(addr, conn):
    print("Connected by", addr)

    full_data = b""
    while True:
        data = conc.recv(BUFFER_SIZE)
        if not data: break
        full_data += data
        # conn.send(data)
            
    time.sleep(0.5)
    conn.sendall(full_data)
    conn.close()

if __name__ == "__main__":
    main()

    #Question 2, server needs to bind , client uses 1 time socket data
