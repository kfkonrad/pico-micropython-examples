from kfkonrad import Pin
import utime
import urandom

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
time_finish = -1


def button_handler(pin):
    global time_finish
    if time_finish == -1:
        time_finish = utime.ticks_ms()


led.value = 1
utime.sleep(urandom.uniform(5, 10))
led.value = 0
time_start = utime.ticks_ms()

button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

while time_finish == -1:
    utime.sleep(0.25)

time_reaction = utime.ticks_diff(time_finish, time_start)
print(f"Your reaction time was {time_reaction} milliseconds!")
