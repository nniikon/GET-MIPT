import RPi.GPIO as GPIO
import time     as time

GPIO.setmode(GPIO.BCM)

LED_GPIO = [2, 3, 4, 17, 27, 22, 10, 9]

for i in LED_GPIO:
    GPIO.setup(i, GPIO.OUT)

n_waves = 3

for j in range(n_waves):
    for i in LED_GPIO:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)

GPIO.cleanup()