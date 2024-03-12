import RPi.GPIO as GPIO
import time     as time

GPIO.setmode(GPIO.BCM)

LED_GPIO = [2,  3,  4,  17, 27, 22, 10, 9 ]
AUX_GPIO = [24, 23, 25, 19, 16, 26, 20, 21]

for i in LED_GPIO:
    GPIO.setup(i, GPIO.OUT)

for i in AUX_GPIO:
    GPIO.setup(i, GPIO.IN)

while (True):
    for i in range(8):
        GPIO.output(LED_GPIO[i], GPIO.input(AUX_GPIO[i]))

GPIO.cleanup()