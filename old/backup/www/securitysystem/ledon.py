import RPi.GPIO as GPIO
import time

# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD) 
# set up GPIO output channel  
ledPin = 7
GPIO.setup(ledPin, GPIO.OUT)


# blink GPIO17 50 times  
GPIO.output(ledPin,GPIO.HIGH)  
time.sleep(5)
GPIO.output(ledPin,GPIO.LOW)

GPIO.cleanup()   
