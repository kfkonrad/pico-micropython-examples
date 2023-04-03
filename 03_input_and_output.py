import machine
import utime

led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

was_pressed = False
change_counter = 0

while True:
    is_pressed = button.value() == 1
    led_external.value(is_pressed)
    if was_pressed ^ is_pressed:
        change_counter += 1
        print(f"Button state changed {change_counter}:", end=" ")
        print("PRESSED" if is_pressed else "RELEASED")
    was_pressed = is_pressed
