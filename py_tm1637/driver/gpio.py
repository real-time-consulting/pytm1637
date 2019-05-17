
from collections import namedtuple

Library = namedtuple('Library', 'instance name')

GPIO_LIBS = ['gpiozero', 'rpi']


def import_gpio_lib(libraries):
    for gpio_lib in libraries:
        try:
            return Library(__import__(gpio_lib), gpio_lib)
        except ImportError:
            continue
    return Library(None, 'None')

module = import_gpio_lib(GPIO_LIBS)

if module.name == 'gpiozero':
    

    class Pin:
        def __init__(self, pin_id, mode='in'):
            self.pin = module.instance.OutputDevice(Converter[pin_id])

        @property.setter
        def state(self, value):
            self.pin.value(value)


if module.name == 'rpi':


    class Pin:
        pass


else:
    raise ImportError(
            'GPIO wrapper needs at least {} modules'.format(GPIO_LIBS))


Converter = {
    11:17}
    
