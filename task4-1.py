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

try:
    while (True):
        num = input("Введите число от 0 до 255: ")
        
        try:
            intnum = int(num)
            if (0 <= intnum and intnum <= 255):
                binary_num = num_to_bin(intnum)
                voltage = float(num) * 3.3 / 256.0
                for i in range(0, 8):
                    GPIO.output(DAC_GPIO[i], binary_num[i])
                print(f"V = : {voltage}")
            else:
                print("Ошибка ввода, попробуйте еще раз")
        except Exception:
            if (num == 'q'):
                print("Пока!")
                break
            else:
                print("Ошибка ввода, попробуйте еще раз")
finally:
    GPIO.output(DAC_GPIO, 0)
    GPIO.cleanup()