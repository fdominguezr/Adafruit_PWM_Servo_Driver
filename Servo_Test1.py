from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x70)
pwm.setPWMFreq(50)

while (True):
   pwWidth = raw_input("Enter a pulse width value between 110 and 480: ")
   if puWidth > 109 and puWidth < 481:
	print"OK"
	pwm.setPWM(0, 0, puWidth)
   else:
	print"Invalid pulse width!"
