"""
This script demonstrates how SimpleNet can be
used to easily create a networking project with
just minimal code.
"""
#########################################################

#Code Author: OmniBean
#Go to:
#http://www.omnibean.96.lt/
#for more by OmniBean.

#########################################################

from simplenet import *

#host = input('Enter hostname: ')
#port = int(input('Enter port number: '))
host(54215,1)
server_send('Hello Client!',1)
input('Done!')
g = server_receive()
input('Received: '+g)
