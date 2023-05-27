from kfkonrad import Pin
import utime
import urandom

led = Pin(15, Pin.OUT)
buttons = [Pin(gpio, Pin.IN, Pin.PULL_DOWN) for gpio in (14, 13)]
time_finish = None

winner = None


def button_handler(pin):
    global time_finish, winner
    if not time_finish:
        time_finish = utime.ticks_ms()
        winner = pin


led.value = 1
utime.sleep(urandom.uniform(5, 10))
led.value = 0
time_start = utime.ticks_ms()

for b in buttons:
    b.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

while not time_finish:
    utime.sleep(0.25)

time_reaction = utime.ticks_diff(time_finish, time_start)
print(f"Player {buttons.index(winner) + 1} won!")
print(f"Your reaction time was {time_reaction} milliseconds!")
