import machine


class Pin(machine.Pin):
    @property
    def value(self):
        return super().value()

    @value.setter
    def value(self, arg):
        super().value(arg)

    def __eq__(self, other):
        return repr(self) == repr(other)
