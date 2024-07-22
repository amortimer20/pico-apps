from machine import ADC, Pin, PWM

light_sensor = ADC(26)
calibration_value = light_sensor.read_u16()

red_pin = PWM(Pin(2))
green_pin = PWM(Pin(3))
blue_pin = PWM(Pin(4))

red_pin.freq(5000)
green_pin.freq(5000)
blue_pin.freq(5000)

while True:
    print(light_sensor.read_u16())

    if light_sensor.read_u16() < calibration_value - 3000:
        red_pin.duty_u16(2560)
        green_pin.duty_u16(25600)
        blue_pin.duty_u16(20480)
    else:
        red_pin.duty_u16(0)
        green_pin.duty_u16(0)
        blue_pin.duty_u16(0)