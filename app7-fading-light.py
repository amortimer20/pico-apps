from machine import Pin, PWM

led = PWM(Pin(25))
led.freq(5000)


while True:
    for n in range(0, 65536):
        led.duty_u16(n)

    for n in range(65536, 0, -1):
        led.duty_u16(n)