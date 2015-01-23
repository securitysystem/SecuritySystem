from xmh import XDocument
configF = XDocument('controlpanel.conf')
serverName = configF.getElement('servername')
gre = configF.getElement('greeting')

class Security:
    def do_command(c):
##        print(c)
        if (c=='kill'):
            import sys
            import time
            print('The system is going down for shutdown...NOW!')
            time.sleep(3)
            sys.exit()
        
    def excecute(command,n):
        print(n,'requested command: ',command)
        _c = command.split('$')
        cmd = _c[1]
        passw = _c[0]
        configF = XDocument('controlpanel.conf')
        apassw = configF.getElement('password')
        print(passw,apassw)
        if (passw == apassw):
            print('Server authenticated',n,'to excecute command: ',cmd)
            Security.do_command(cmd)
    

import SimpleNetPlus.udp as s
import SimpleNetPlus.tcp as t
PORT = int(configF.getElement('port'))
SERVER_ID = serverName
print(''+SERVER_ID+'. Waiting for clients on '+str(PORT))
s.server.listen(PORT)
while True:
    try:
        data,addr = s.server.receive_broadcast()
        #print ('Received: '+str(data)+' from '+str(addr))
        name = data
        print(str(addr)+' was detected as '+name)
        #print('Sending reply...')
        #s.client.connect(PORT)
        gr = '''The '''+SERVER_ID+''' #'''+SERVER_ID+''' Welcomes You!\n'''+gre
        t.connect(addr[0],PORT+1)
        t.send(gr)
        comm = t.receive()
        t.close()
        sender = name
        Security.excecute(comm,sender)
        #s.client.broadcast('The Tomato Server Welcomes You!',PORT)
        #input('Hit Enter to continue...')
    except Exception as ex:
        print('Client caused server crash - ',ex)
