from machine import Pin
from utime import sleep

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("    pressed :)")
    else:
        print("Not pressed :(")
    sleep(0.1)