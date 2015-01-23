import simplenet as n

print('Starting Client...')
n.connect('THUNDERSTORM',8001,1)
while True:
    m = input('Enter Something to send: ')
    n.send(m)
    print(m)
