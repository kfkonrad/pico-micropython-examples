from kfkonrad import Pin

led_external = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

was_pressed = False
change_counter = 0

while True:
    is_pressed = button.value == 1
    led_external.value = is_pressed
    if was_pressed ^ is_pressed:
        change_counter += 1
        print(f"Button state changed {change_counter}:", end=" ")
        print("PRESSED" if is_pressed else "RELEASED")
    was_pressed = is_pressed
