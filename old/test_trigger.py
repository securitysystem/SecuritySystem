import os
import threading
import time

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
    #Logic, switch loop etc
    msg = """<br>
        Everything OK. <br>
    """
    return msg

outputPath = '/var/www/securitysystem/logfile.pw'
triggerFile = '/var/www/securitysystem/trigger.pw'
while True:
    time.sleep(1)
    #if(os.path.isfile(triggerPath)):
    #    print('Trigger Detected.')
    #os.remove(triggerPath)
    currentLog = file_get_contents('logfile.log')
    currentLog = currentLog + nowstate()
    file_put_contents(outputPath,currentLog)
    print('Putting Contents...')
    
    
    
    
