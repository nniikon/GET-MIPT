import RPi.GPIO as GPIO
import time     as time

GPIO.setmode(GPIO.BCM)

DAC_GPIO = [8, 11, 7, 1, 0, 5, 12, 6]
NUMBER  = [0] * 8

for i in DAC_GPIO: 
    GPIO.setup(i, GPIO.OUT)

#NUMBER = [1, 1, 1, 1, 1, 1, 1, 1] # 255 - 3.25V
#NUMBER = [0, 1, 1, 1, 1, 1, 1, 1] # 127 - 1.68V
#NUMBER = [0, 1, 0, 0, 0, 0, 0, 0] # 64 - 0.87V
#NUMBER = [0, 0, 1, 0, 0, 0, 0, 0] # 32 - 0.46V
#NUMBER = [0, 0, 0, 0, 0, 1, 0, 1] # 5 - 0.11V
#NUMBER = [0, 0, 0, 0, 0, 0, 0, 0] # 0 - 0.05V

for i in range(8):
    GPIO.output(DAC_GPIO[i], NUMBER[i])

time.sleep(10)

for i in DAC_GPIO:
    GPIO.output(i, 0)

GPIO.cleanup()