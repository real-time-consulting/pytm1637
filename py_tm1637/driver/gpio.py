
GPIO_LIBS = ['gpiozero']

for gpio_lib in GPIO_LIBS:
    try:
        instance = __import__('gpio_{}'.format(gpio_lib))
        Pin = instance.Pin
        converter = instance.converter
        break
    except ImportError:
        continue
else:
    raise ImportError(
        'GPIO wrapper needs at least {} modules'.format(GPIO_LIBS))
