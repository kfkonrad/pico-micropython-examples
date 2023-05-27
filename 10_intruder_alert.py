from kfkonrad import Pin
import utime

sensor_pir = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in (26, 22)]
led = Pin(15, Pin.OUT)
buzzer = Pin(14, Pin.OUT)


def pir_handler(pin):
    utime.sleep_ms(100)
    print(f"Alarm on sensor #{sensor_pir.index(pin)}!")
    for i in range(100):
        led.toggle()
        if i % 10 == 0:
            for _ in range(26):
                buzzer.toggle()
                utime.sleep_ms(3)
        utime.sleep_ms(100)


for s in sensor_pir:
    s.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)


while True:
    utime.sleep_ms(20)
