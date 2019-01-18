#!/usr/bin/env python3
import socket
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    google_addr = None

    
    addr_info = socket.getaddrinfo("www.google.com", 80)
    for addr in addr_info:
        #print(addr)
        (family, socktype, proto, canonname, sockaddr) = addr
        if family == socket.AF_INET and socktype == socket.SOCK_STREAM:
            google_addr = addr
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #Question 3, socket option, so_reuseaddr
        #Question 4, it prints: connected by: client IP , port
        #Question 5, It returns None
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            (family, socktype, proto, canonname, sockaddr) = google_addr
            with socket.socket(family, socktype) as proxy_end:
                proxy_end.connect(sockaddr)
                send_full_data = b""
                while True:
                    data = conc.recv(BUFFER_SIZE)
                    if not data: break
                    senf_full_data += data

                proxy_end.sendall(send_full_data)
                proxy_end.shutdown(socket.SHUT_WR)

                while True:
                    data = proxy_end.recv(BUFFER_SIZE)
                    if not data: break
                    conn.send(data)
            
            time.sleep(0.5)
            conn.close()

if __name__ == "__main__":
    main()

    #Question 2, server needs to bind , client uses 1 time socket data
