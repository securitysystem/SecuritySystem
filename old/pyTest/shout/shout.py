import simplenet as n

def shout(hostwn,data):
    print('Starting shout.py Client...')
    n.connect(hostwn,8001,1)
    m = data
    n.send(m)
    #print(m)
    n.close()
