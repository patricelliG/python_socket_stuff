#!/usr/bin/env python3

"""
server.py

This program is a simple demo of a server client program using sockets in
python3. This particular program does not use a new connection for each
piece of data being sent. Rather, it keeps one connection up for the
duration of the transfer.
"""

import base64
import binascii
import socket

""" Initialze the server to listen on PORT
"""
HOST = ''
PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((HOST, PORT))
except Exception as e:
    print('Failed to bind to port, exiting.')
    print(e)
    exit(1)

""" Now listen and wait for a connection...
"""
sock.listen(1)
conn, addr = sock.accept()
print('connected to host: {} on port: {}'.format(conn.getpeername()[0], addr[1]))

""" We have a connection, now read until the \n, decode and print it.
"""
delimiter = binascii.unhexlify('a0')
encoded_data = bytearray()
while True:
    b = conn.recv(1)
    if b == delimiter:
        print("DELIMITER")
    if b != b'\n' and b != b'':
        encoded_data += b
    elif len(encoded_data) > 0:
        print('recieved: {}'.format(base64.b64decode(encoded_data)))
        encoded_data = bytearray(b'')
