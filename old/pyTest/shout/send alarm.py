import shout
import socket

tpc = 'THUNDERSTORM'
target = socket.gethostbyname(tpc)

shout.shout(target,'Security Breach!!!!!')
