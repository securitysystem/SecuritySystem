from xmh import XDocument
configF = XDocument('server.conf')
serverName = configF.getElement('servername')
gre = configF.getElement('greeting')

import SimpleNetPlus.udp as s
import SimpleNetPlus.tcp as t
PORT = int(configF.getElement('port'))
SERVER_ID = serverName
print(''+SERVER_ID+'. Waiting for clients on '+str(PORT))
s.server.listen(PORT)
while True:
    data,addr = s.server.receive_broadcast()
    #print ('Received: '+str(data)+' from '+str(addr))
    name = data
    print(str(addr)+' was detected as '+name)
    #print('Sending reply...')
    #s.client.connect(PORT)
    gr = '''The '''+SERVER_ID+''' #'''+SERVER_ID+''' Welcomes You!'''+gre
    t.connect(addr[0],PORT+1)
    t.send(gr)
    t.close()
    #s.client.broadcast('The Tomato Server Welcomes You!',PORT)
    #input('Hit Enter to continue...')
