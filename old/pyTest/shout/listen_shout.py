import simplenet as n

print('Starting listen_shout.py Server...')
n.host(8001,1)
#while True:
#    m = n.server_receive()
#    print(m)
#    #input(m)

m = n.server_receive()
input('Received a shout: '+m)
