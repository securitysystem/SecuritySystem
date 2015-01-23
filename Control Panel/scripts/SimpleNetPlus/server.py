#UDP server responds to broadcast packets
#you can have more than one instance of these running
import socket
address = ('', 54545)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind(address)

print ("Listening for data...")
while True:    
    recv_data, addr = server_socket.recvfrom(2048)
    str_data = bytes.decode(recv_data)
    print (addr,':', str_data)
    sendmsg = ""+socket.getfqdn
    server_socket.sendto(str.encode("*"+str_data), addr)
