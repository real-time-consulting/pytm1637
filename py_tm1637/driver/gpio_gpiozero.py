
#import gpiozero

class Pin:
    def __init__(self, pin_id, mode='in'):
        self.pin = gpiozero.OutputDevice(converter[pin_id])

    @property
    def state(self, value):
        self.pin.value(value)
    

converter = {
    11: 17}
