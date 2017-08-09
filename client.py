#!/usr/bin/env python3

"""
This program is a simple demo of a server client program using sockets in
python3. This particular program does not use a new connection for each
piece of data being sent. Rather, it keeps one connection up for the
duration of the transfer.
"""

import time
import base64
import socket

""" Set up the connection to the server. NOTE, the server must be running
before the client tries to connect to it otherwise it will throw an
error. One could choose to handle such an exception.
"""

SERVER_IP = '192.168.1.100'
SERVER_PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((SERVER_IP, SERVER_PORT))
except Exception as e:
    print('Could not connect to the server, is server.py running?')


for i in range(1000):
    """ This is dummy data, here we use the time of day.
    """
    data = time.asctime()

    """ Before sending it out, it needs to be encoded to prevent it getting
    trunked by anyone in transit.
    """
    encoded_data = base64.b64encode(data.encode('UTF-8'))

    """ Now we send the data over the socket we opened earlier. """
    try:
        sock.sendall(encoded_data)
    except Exception as e:
        print('Could not send data to server. Exiting.')
        exit(1)
