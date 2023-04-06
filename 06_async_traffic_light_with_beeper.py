from kfkonrad import Pin
import uasyncio

led_red = Pin(15, Pin.OUT)
led_amber = Pin(14, Pin.OUT)
led_green = Pin(13, Pin.OUT)

button = Pin(16, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(12, Pin.OUT)

global button_pressed
button_pressed = False

async def read_button():
    global button_pressed
    while True:
        if button.value == 1:
            button_pressed = True
        await uasyncio.sleep(0.01)


async def handle_pedestrian_traffic():
    global button_pressed
    led_red.value = 1
    led_amber.value = 0
    led_green.value = 0
    if button_pressed is True:
        for i in range(10):
            buzzer.value = 1
            await uasyncio.sleep(0.005)
            buzzer.value = 0
            await uasyncio.sleep(0.2)
        button_pressed = False

async def traffic_lights():
    while True:
        await handle_pedestrian_traffic()
        led_red.value = 1
        await uasyncio.sleep(5)
        led_amber.value = 1
        await uasyncio.sleep(2)
        led_red.value = 0
        led_amber.value = 0
        led_green.value = 1
        await uasyncio.sleep(5)
        led_green.value = 0
        led_amber.value = 1
        await uasyncio.sleep(5)
        led_amber.value = 0

loop = uasyncio.get_event_loop()
group = uasyncio.gather(read_button(), traffic_lights())
results = loop.run_until_complete(group)
