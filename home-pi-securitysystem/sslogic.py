def panic():
	import os
	os.system('sudo rm /var/www/securitysystem/pic/panic.png')
	os.system('sudo python /var/www/securitysystem/pic.py /var/www/securitysystem/pic/panic.png')
def get():
	try:
		import serial
		ser = serial.Serial('/dev/ttyACM0', 9600)
		recv = ser.readline()
	except:
		recv = 'unknown: No Media Connected'
	#recv = str(recv)
	recv = recv.decode('utf-8')
	#recv.replace('\r','')
	#recv.replace('\n','')
	return recv

def correct(txt,goal):
	if (goal in txt):
		return goal
	if (txt in goal):
		return goal
	else:
		return txt
