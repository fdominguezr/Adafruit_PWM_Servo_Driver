# This is a simple test of Servo with Raspberry Pi and Hatalogico board
# In this test the software just ask you and moves the servo between 0 and 180 degrees.
# You need to connect the servo signal input to PWM0 pin in Hatalogico board
# More info here http://letsmakerobots.com/content/pwm-control-raspberry-pi-a-servo-second-test-hatal%C3%B3gico-board

# First we import Adafruit's PWM driver with I2C communication
from Adafruit_PWM_Servo_Driver import PWM
import time
import sys
import select

def heardEnter():
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
			
            return True
    return False
   
# Sets I2C address to 0x70 that's the standard for Hatalogico
pwm = PWM(0x70)
pwm.setPWMFreq(50)

# Moves servo to 0 degrees position. Please note 120 as minimum value is the approx value of 0 degrees for my servo tested.
# You should test/calibrate each servo to maximize its movement span while not stretching it too much.
# For more info check this article: http://letsmakerobots.com/node/39297

position = 90

while (True):
#Now the program will ask for an angle so Raspi can move servo from 0 degrees to 180 degrees
	print ("Press key 'a' for less angle or key 's' for more angle")
	keypress = heardEnter()
	if (keypress == 'a' and position > -1):
		position = position - 1
	elif (keypress == 's' and position < 181):
		position = position +1
	if  position > -1 and  position < 181:
			print "Desired position is: " , position
			puWidth = 2* position + 120
			pwm.setPWM(0,0, puWidth)
	else:
		if position == 180:
			print "Position already 180. Decrease angle pressing key 'a'"
		if position == 0:
			print "Position already 0. Increase angle pressing key 's'"
	time.sleep(0.5)