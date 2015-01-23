import simplenet as n

print('Starting Client...')
n.connect('192.168.0.8',8001,1)
while True:
    m = input('Enter Something to send: ')
    n.send(m)
    print(m)
