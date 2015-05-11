# This is a simple test of Servo with Raspberry Pi and Hatalogico board
# In this test the software just ask you and moves the servo between 0 and 180 degrees.
# You need to connect the servo signal input to PWM0 pin in Hatalogico board
# More info here http://letsmakerobots.com/content/pwm-control-raspberry-pi-a-servo-second-test-hatal%C3%B3gico-board

# First we import Adafruit's PWM driver with I2C communication
from Adafruit_PWM_Servo_Driver import PWM
import time

# Sets I2C address to 0x70 that's the standard for Hatalogico
pwm = PWM(0x70)
pwm.setPWMFreq(50)


# Moves servo to 0 degrees position. Please note 120 as minimum value is the approx value of 0 degrees for my servo tested.
# You should test/calibrate each servo to maximize its movement span while not stretching it too much.
# For more info check this article: http://letsmakerobots.com/node/39297
while (True):
#Now the program will ask for a number so we can move servo from 0 degrees to 180 degrees
	puWidth = input('Enter a pulse width value between 0 and 180 degrees: ')
	if puWidth > 0 and puWidth < 181:
		print'OK'
		puWidth = 2*puWidth + 120
		pwm.setPWM(0,0,puWidth)
	else:
		print'Invalid pulse width!'
