from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x70)
pwm.setPWMFreq(50)

while (True):
	pwm.setPWM(0, 0, 120)
	time.sleep(0.3)
	pwm.setPWM(0,0,290)
	time.sleep(0.3)
	pwm.setPWM(0,0,480)
	time.sleep(0.3)
