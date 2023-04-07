from kfkonrad import Pin
from utime import sleep

led_red = Pin(15, Pin.OUT)
led_amber = Pin(14, Pin.OUT)
led_green = Pin(13, Pin.OUT)

button = Pin(16, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(12, Pin.OUT)

global button_pressed
button_pressed = False

def read_button(_):
    global button_pressed
    button_pressed = True

def handle_pedestrian_traffic():
    global button_pressed
    led_red.value = 1
    led_amber.value = 0
    led_green.value = 0
    if button_pressed is True:
        for i in range(10):
            buzzer.value = 1
            sleep(0.005)
            buzzer.value = 0
            sleep(0.2)
        button_pressed = False

def traffic_lights():
    while True:
        handle_pedestrian_traffic()
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

button.irq(trigger=Pin.IRQ_RISING, handler=read_button)
traffic_lights()
