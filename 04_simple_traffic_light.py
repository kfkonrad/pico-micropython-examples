from kfkonrad import Pin
from utime import sleep

led_red = Pin(15, Pin.OUT)
led_amber = Pin(14, Pin.OUT)
led_green = Pin(13, Pin.OUT)

while True:
    led_red.value = 1
    sleep(5)
    led_amber.value = 1
    sleep(2)
    led_red.value = 0
    led_amber.value = 0
    led_green.value = 1
    sleep(5)
    led_green.value = 0
    led_amber.value = 1
    sleep(5)
    led_amber.value = 0
