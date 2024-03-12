import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup (16, GPIO.OUT)
GPIO.output(16, 0)

GPIO.setup (24, GPIO.IN)

while True:
    GPIO.output(16, GPIO.input(24))
