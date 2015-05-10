# This is a simple test of Servo with Raspberry Pi and Hatalogico board
# In this test the software just commands to move the servos between 0 degrees, 90 degrees and 180 degrees with 0.3 seconds between each position.
# You need to connect the servo signal to PWM0 pin in Hatalogico board
# More info here http://letsmakerobots.com/content/pwm-control-raspberry-pi-a-servo-second-test-hatal%C3%B3gico-board

# First we import Adafruit's PWM driver with I2C communication
from Adafruit_PWM_Servo_Driver import PWM
import time

# Sets I2C address to 0x70 that's the standard for Hatalogico
pwm = PWM(0x70)

#Sets the frequency of PWM output to the standard for most servos: 50Hz (2 ms)
pwm.setPWMFreq(50)

while (True):
#Now we move servo by 90 degrees steps from 0 degrees to 180 degrees with 0.3 seconds of wait to give time so the servo can moves

# Moves servo to 0 degrees position. Please note 120 is the approx value of 0 degrees for my servo tested.
# You should test/calibrate each servo to maximize its movement span while not stretching it too much.
# For more info check this article: http://letsmakerobots.com/node/39297
	pwm.setPWM(0, 0, 120)
# Waits 0.3 seconds to give time to servo reach its position
	time.sleep(0.3)
# Moves servo to 90 degrees position
	pwm.setPWM(0,0,290)
	time.sleep(0.3)
# Moves servo to 180 degrees position
	pwm.setPWM(0,0,480)
	time.sleep(0.3)
