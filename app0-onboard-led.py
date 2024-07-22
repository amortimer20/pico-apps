from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    sleep(1)
    print(led.value())
    led.value(0)
    sleep(1)
    print(led.value())