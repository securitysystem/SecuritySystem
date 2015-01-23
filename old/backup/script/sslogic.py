def get():
	try:
		import serial
		ser = serial.Serial('/dev/ttyACM0', 9600)
		recv = ser.readline()
	except:
		recv = 'unknown: No Media Connected'
	recv = str(recv,'ascii')
	#recv.replace('\r','')
	#recv.replace('\n','')
	return recv
