from machine import Pin
from random import randint
from utime import sleep, ticks_ms

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)


while True:
    led.value(0)
    print("Wait for the light...")
    
    wait_time = randint(3, 5)
    sleep(wait_time)
    start_time = ticks_ms()
    
    led.value(1)
    
    while button.value() == 0:
        pass
    
    led.value(0)
    react_time = ticks_ms() - start_time
    print(f"Great job! Your reaction time was {react_time}")
    sleep(5)