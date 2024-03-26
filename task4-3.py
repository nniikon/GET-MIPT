import RPi.GPIO as GPIO
import time     as time

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
p = GPIO.PWM(9, 1000)
p.start(0)

try:
    while (True):
        try:
            f = int(input())
            p.ChangeDutyCycle(f)
            voltage = 3.3*f/100
            print(f"V = {voltage}")
        except Exception:
            print("Плохой ввод")
finally:
    GPIO.cleanup()