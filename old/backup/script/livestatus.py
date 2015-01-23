import os
import threading
import time
import datetime


status = 'none'
def file_put_contents(path,contents):
    f = open(path,'w+')
    f.write(contents)
    f.close()

def file_get_contents(path):
    f = open(path)
    c = f.read()
    f.close()
    return c
def nowstate():
    global status
    now = datetime.datetime.now()
    now = str(now)
    #Logic, switch loop etc
    status = 'safe'
    ww = 'The Inner workings of the script currently perform live updates, but is not yet taking hardware input.'
    msg = 'Direct Message from Script: '+ww
    if status == 'safe':
       msg = "<br>Everything OK - "+now+"<br>"+msg+"<br>"
       return msg

outputPath = '/var/www/securitysystem/logfile.pw'
triggerFile = '/var/www/securitysystem/trigger.pw'
statusFile = '/var/www/securitysystem/status.pw'
print('Security System Running...')
while True:
    time.sleep(2)
    #if(os.path.isfile(triggerPath)):
    #    print('Trigger Detected.')
    #os.remove(triggerPath)
    currentLog = file_get_contents('logfile.log')
    currentLog = currentLog + nowstate()
    currentStatus = nowstate()
    file_put_contents(statusFile,currentStatus)

    if (status != 'safe'):
        file_put_contents(outputPath,currentLog)
        file_put_contents('logfile.log',currentLog)
    #print('Putting Contents...')
    print('Status: '+currentStatus)