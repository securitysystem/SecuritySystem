import simplenet as n

print('Starting Server...')
n.host(8001,1)
while True:
    m = n.server_receive()
    print(m)
