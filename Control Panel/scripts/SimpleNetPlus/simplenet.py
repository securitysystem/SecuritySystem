
#########################################################
#SIMPLENET PLUS v1.2





#########################################################
"""
The SimpleNet Library for Python 3 is a library
that allows anyone to easily set up networking in Python using sockets.
Everything is predefined, check out the demos for more information.
Read the Documentation for more information and a tutorial.


"""

#SimpleNet Plus Package - SimpleNet Module

import os
import socket # Import socket module

s = socket.socket()         # Create a socket object
client = 'Nx'
address = 'Nx'
waddress = 'Nx'
cport = 0
localhost = 'Nx'

def gethostname():
    return socket.gethost()

def getdns():
    return socket.getfqdn()
