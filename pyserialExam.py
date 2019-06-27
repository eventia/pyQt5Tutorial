# https://kamang-it.tistory.com/entry/Arduino-Python%EC%9C%BC%EB%A1%9C-UARTSerial%ED%86%B5%EC%8B%A0%ED%95%98%EA%B8%B0

import serial

ser = serial.Serial(
    port='com10',
    baudrate=9600,
)

while True:
    if ser.readable():
        res = ser.readline()
        print(res.decode()[:len(res)-1])
