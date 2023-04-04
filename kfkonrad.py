import machine

class Pin(machine.Pin):
    @property
    def value(self):
        return super().value()
    @value.setter
    def value(self, arg):
        super().value(arg)
