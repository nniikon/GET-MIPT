import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.output(16, 0)

# WARNING! cringe
for i in range (0, 10):
    for i in range(0, 1000000):
        if (i < 500000):
            GPIO.output(16, 0)
        else:
            GPIO.output(16, 1)

GPIO.output(16, 0)