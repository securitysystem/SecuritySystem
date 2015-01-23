
#########################################################
#SIMPLENET PLUS v1.2





#########################################################
"""
The SimpleNet Library for Python 3 is a library
that allows anyone to easily set up networking in Python using sockets.
Everything is predefined, check out the demos for more information.
Read the Documentation for more information and a tutorial.


"""

#SimpleNet Plus Package - UDP Module


#Client
class client:
    client_socket = None
    """Set up broadcast on a port"""
    def connect(port):
        global client_socket
        #UDP client broadcasts to server(s)
        import socket
        address = ('<broadcast>', port)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        #data = socket.getfqdn()+" pinging..."
        #client_socket.sendto(str.encode(data), address)
    """Broadcast data on a port"""
    def broadcast(data,port):
        global client_socket
        #UDP client broadcasts to server(s)
        import socket
        address = ('<broadcast>', port)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        #data = socket.getfqdn()+" pinging..."
        client_socket.sendto(str.encode(data), address)

    """Get data and address in (data,address) tuple"""
    def receive_broadcast(port=None,leng=None):
        recv_data = None
        addr = None
        global client_socket
        if client_socket == None:
            connect(port)
        if (leng != None):
            recv_data, addr = client_socket.recvfrom(leng)
        else:
            recv_data, addr = client_socket.recvfrom(2048)
        str_data = bytes.decode(recv_data)
        return (str_data,addr)
#Server
class server:
    server_socket = ''
    """Initialize listening for broadcasts on a port"""
    def listen(port):
        global server_socket
        import socket
        address = ('', port)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        server_socket.bind(address)
    """Receive Broadcast in (data,address) tuple"""
    def receive_broadcast(leng=None):
        recv_data = None
        addr = None
        global server_socket
        if (leng!=None):
            recv_data, addr = server_socket.recvfrom(leng)
        else:
            recv_data, addr = server_socket.recvfrom(2048)
        str_data = bytes.decode(recv_data)
        return (str_data,addr)
        #print (addr,':', str_data)
        #sendmsg = ""+socket.getfqdn()
        #server_socket.sendto(str.encode("*"+str_data), addr)

    #"""Broadcast stub"""
    #def broadcast():
    #    pass
