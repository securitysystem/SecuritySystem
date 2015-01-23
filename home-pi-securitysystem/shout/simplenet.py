
#########################################################

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


def host(port, showdata=None, backlog=None):
    global s,client, address, waddress, cport, localhost
    cport = int(port)
    mhost = host = socket.gethostname()
    s = socket.socket()         # Create a new socket object
    s.bind((host,port))
    #print('Port is ',cport)
    if showdata != None:
        print('Waiting for connection at '+str(host)+' on port '+str(port))
    if backlog != None:
        s.listen(backlog)
    else:
        s.listen(5)
    client, address = s.accept()
    waddress = address
    if showdata != None:
        print('Got Connection from: '+str(address)+' on port '+str(cport))

def connect(thost, port, showdata=None):
    global s, client, address, waddress, cport, localhost
    port = int(port)
    cport = port
    #print('Port is ',cport)
    localhost = host = socket.gethostname()
    s = socket.socket()         # Create a new socket object
    if showdata != None:
        print('Waiting for connection at: '+str(thost)+' on port '+str(cport))
    s.connect((thost, port))
    waddress = thost
    if showdata != None:
        print('Connected to: '+str(waddress)+' on port '+str(cport))

def send(msg, showdata=None):
    global s,client, address, waddress, cport, localhost
    if showdata != None:
        print('Target Address:',waddress)
        print('Target Port:',cport)
    #print()
    #s.connect((waddress, cport))
    
    data = str.encode(str(msg))
    s.send(data)
    if showdata != None:
        print('Sent '+waddress+':',str(msg))

def receive(size=None, showdata=None):
    global s,client, address, waddress, cport, localhost
    if showdata != None:
        print('Target Address:',waddress)
        print('Target Port:',cport)
    #s.connect((waddress, cport))
    if size != None:
        data = s.recv(size)
    else:
        data = s.recv(5000)
        
    if showdata != None:
        print('Received from '+address+':',bytes.decode(data))
    return bytes.decode(data)

def server_send(msg, showdata=None):
    global s, client, address, waddress, cport, localhost
    if showdata != None:
        print('Target Address:',waddress)
        print('Target Port:',cport)
    #print()
    #s.connect(waddress, cport))
    
    data = str.encode(str(msg))
    client.send(data)
    if showdata != None:
        print('Sent '+waddress[0]+':',str(msg))

def server_receive(size=None, showdata=None):
    global s,client, address, waddress, cport, localhost
    if showdata != None:
        print('Target Address:',waddress)
        print('Target Port:',cport)
    #s.connect((waddress, cport))
    if size != None:
        data = client.recv(size)
    else:
        data = client.recv(5000)
        
    if showdata != None:
        print('Received from '+address+':',bytes.decode(data))
    return bytes.decode(data)


def close(showdata=None):
    global s,client, address, waddress, cport, localhost
    try:
        client.close()
    except:
        s.close()
    if showdata != None:
        print('Closed connection with '+addr+' on port '+cport)
