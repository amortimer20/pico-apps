from machine import ADC, Pin
from utime import sleep

light_sensor = ADC(26)

while True:
    print(light_sensor.read_u16())
    sleep(0.1)