#Security System Script
import os
import threading
import time
import datetime


status = 'none'
def file_put_contents(path,contents):
    f = open(path,'w+')
    f.write(contents)
    f.close()

prev = ''
ms = ''
panictime = ''
def file_get_contents(path):
    f = open(path)
    c = f.read()
    f.close()
    return c
def nowstate():
	global status,prev,panictime,ms
	arm = open('/var/www/securitysystem/arm.pw').read()
	armed = False
	panic = False
	if (arm == 'armed'):
		armed = True
	if (arm == 'panic'):
		armed = True
		panic = True
	if (arm== 'disarm'):
		panic = False
		armed=False

	now = datetime.datetime.now()
	now = str(now)
    #Logic, switch loop etc
	import sslogic
	rs = sslogic.correct(sslogic.get().replace('\r\n','').replace('\n','') ,'safe')
	status = "<br>"+rs + " - "+ now + "<br>"
	ms = rs
		
	if rs == 'safe' and not panic:
		msg = "<br>Everything OK - "+now+"<br>"
		if armed and not panic:
			msg = '<br>Armed - '+now+'<br>'
	elif rs == 'ALERT' or panic:
		if rs == 'ALERT':
			panictime = now
			sslogic.panic()
		if armed:
			now = 'Last Security Breach: '+panictime
		if armed:
			#print('sb')
			msg = '<br>PANIC! Security Breach - '+now+'<br><img src="pic/panic.png">'
			open('/var/www/securitysystem/arm.pw','w+').write('panic')
		else:
			msg = '<br>Circuit Opened - '+now+'<br>'
	else:
		import sys
		msg = 'Status Unspecified'
		if (sys.argv[1]=='debug'):
			msg = rs
	prev = rs
	return msg

outputPath = '/var/www/securitysystem/logfile.pw'
triggerFile = '/var/www/securitysystem/trigger.pw'
statusFile = '/var/www/securitysystem/status.pw'
#print('Security System Running...')
while True:
    time.sleep(2)
    #if(os.path.isfile(triggerPath)):
    #    print('Trigger Detected.')
    #os.remove(triggerPath)
    currentLog = file_get_contents('/home/pi/securitysystem/logfile.log')
    currentStatus = nowstate()
    currentLog = currentLog + currentStatus
    file_put_contents(statusFile,currentStatus)

    if (ms != 'safe'):
        file_put_contents(outputPath,currentLog)
        file_put_contents('logfile.log',currentLog)
    print('Status: '+currentStatus)
