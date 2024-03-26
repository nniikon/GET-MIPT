import RPi.GPIO as GPIO
import time     as time

def num_to_bin(num):
    str = bin(num)[2:].zfill(8)
    list = [int(digit) for digit in str]
    return list


GPIO.setmode(GPIO.BCM)

LED_GPIO = [2, 3 ,  4,  17, 27, 22, 10, 9]
DAC_GPIO = [8, 11,  7,  1 , 0 , 5 , 12, 6]

GPIO.setup(DAC_GPIO, GPIO.OUT)

num = 1
increment = 1

period = 0.0

while (True):
    try:
        period = float(input("Введите период в секундах: "))
        break
    except Exception:
        print("Неверный ввод")

while (True):
    if (num == 255 or num == 0):
        increment = -increment

    binary_num = num_to_bin(num)
    voltage = float(num) * 3.3 / 256.0
    for i in range(0, 8):
        GPIO.output(DAC_GPIO[i], binary_num[i])
    print(f"V = : {voltage}")

    num += increment
    time.sleep(period/512)


GPIO.output(DAC_GPIO, 0)
GPIO.cleanup()