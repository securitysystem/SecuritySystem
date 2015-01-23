import SimpleNetPlus.udp as s
import SimpleNetPlus.tcp as t
import SimpleNetPlus.net as n
import getpass
import sys
name = getpass.getuser()+' on '+n.getdns()#input ('Enter your login name: ')
PORT = int(sys.argv[1]) #int(input('Enter server port: '))
command = sys.argv[2]
print('Security System Control Panel Client')
#s.server.listen(PORT)
#data,addr = s.server.receive_broadcast()
#print ('Received: '+str(data))
#print('Client is at: '+str(addr))
#print('Sending reply...')
s.client.connect(PORT)
print('Pinging for Security Systems on '+str(PORT)+'...')
s.client.broadcast(name,PORT)
t.host(PORT+1)
msg = t.server_receive()
t.server_send(command)
t.close()
print('Server Returned:',msg)
#input('Hit Enter to continue...')
