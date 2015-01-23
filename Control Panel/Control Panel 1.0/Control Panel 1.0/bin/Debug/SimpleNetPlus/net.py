
#########################################################
#SIMPLENET v1.2



#Code Author: OmniBean
#Go to:
#http://www.omnibean.96.lt/
#for more by OmniBean.

#########################################################
"""
The SimpleNet Library for Python 3 is a library written by OmniBean
that allows anyone to easily set up networking in Python using sockets.
Everything is predefined, check out the demos for more information.
Read the Documentation for more information and a tutorial.


"""

#SimpleNet by OmniBean

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
