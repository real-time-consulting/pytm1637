
class LedDisplay(object):
    
    _SEGMENTS = bytearray(b'\x3F\x06\x5B\x4F\x66\x6D\x7D\x07\x7F\x6F\x77\x7C\x39\x5E\x79\x71\x3D\x76\x06\x1E\x76\x38\x55\x54\x3F\x73\x67\x50\x6D\x78\x3E\x1C\x2A\x76\x6E\x5B\x00\x40\x63')

    CONVERSION_TABLE = {
        '0': 0x3f,
        '1': 0x06,
        '2': 0x5b,
        '3': 0x4f,
        '4': 0x66,
        '5': 0x6d,
        '6': 0x7d,
        '7': 0x07,
        '8': 0x7f,
        '9': 0x6f,
        'a': 0x77,
        'b': 0x7c,
        'c': 0x39,
        'd': 0x5e,
        'e': 0x79,
        'f': 0x71,
    }
    DISPLAYS = 4 # Specifies the number of displays
    COLONS = 1   # Specifies the number of colon LED on the display
    POINTS = 0   # Specifies the number of point LED on the display

    def __init__(self):
        '''Initialize the LedDisplay class
        '''
        self.FORMAT_STRING = '{{:>{0:d}.{0:d}s}}'.format(self.DISPLAYS)

    def write(self, segments, colon = 0, point = 0):
        '''Write segments to LED display controller chip.

        Args:
            * segments (:obj:`bytearray`): An array of segments which need to
              be written to display controller chip. The behaviour is undefined
              if the array is bigger then the number of available displays.
            * colon (:obj:`int`, *optional*): This argument is used to specify
              which colons need to be light up. The integer is interpreted as
              a bit mask. If the argument is `0` then no colon LED will light 
              up. LSB bit of the integer is associated with the colon on the 
              right side. Default is all off.
            * point (:obj:`int`, *optional*): This argument is used to specify
              which point need to be light up. The integer is interpreted as
              a bit mask. If the argument is `0` then no point LED will light 
              up. LSB bit of the integer is associated with the point on the 
              right side. Default is all off.
        '''
        raise NotImplementedError('Abstract method not implemented')

    def encode_string(self, string):
        '''Convert an up to 4 character length string containing 0-9, a-z,
        space, dash, star to an array of segments.
        
        Args:
            * string (:obj:`str`): A string which needs to be converted to
              segments
        '''
        return bytearray(map(self.encode_char, 
                             self.FORMAT_STRING.format(string)))

    def encode_char(self, char):
        '''Encode a character to a segment.
        
        Args:
            * char (:obj:`str`): A single char that needs to be converted to
              segment.

        Raises:
            * ValueError: When the char argument cannot be converted to a 
              segment.

        Returns:
            Segment information which can be passed to Led Display chip.
        '''
        try:
            return self.CONVERSION_TABLE[char]
        except KeyError:
            raise ValueError('Character out of range: {:d} \'{:s}\''.format(ord(char), char))

    def text(self, text):
        self.write(self.encode_string(text))

    def number(self, num, leading_zero = False):
        if not leading_zero:
            string = '{: >4d}'.format(num)
        else:
            string = '{:0>4d}'.format(num)
        self.text(string)

    def temperature(self, temp):
        '''Display temperature information on the display.

        Format the temperature information and add the `*C` Celsius degree
        sign. If the temperature information cannot fit the display then two
        things may happen:
            * If the temperature is negative then the 'lo' text is shown.
            * If the temperature is positive or zero then the 'hi' text is
              shown.

        Args:
            * temp (:obj:`int`): Temperature in Celsius degrees.
        '''
        string = '{:d}*C'.format(temp)

        if len(string) > self.DISPLAYS:
            if temp < 0:
                string = 'lo'
            else:
                string = 'hi'
        self.text(string)

    def time(self, hour, minute, seconds, flash = True):
        '''Display time information on the display.

        If the current LED Display has 4 display then HH:MM will be shown. If
        the current LED Display has 6 or more displays then HH:MM:SS will be
        shown.

        Args:
            * hour (:obj:`int`): Hour information
            * minute (:obj:`int`): Minute information
            * seconds (:obj:`int`): Seconds information
            * flash (:obj:`boolean`, *optional*): If the argument is `True` 
              then the colon LEDs will be flashed each second. If the argument 
              is `False` then the colon LEDs will be constantly on. The default
              value is `True`.
        '''
        if self.DISPLAYS >= 6:
            string = '{:02d}{:02d}{:02d}'.format(hour, minute, seconds)
        else: 
            string = '{:02d}{:02d}'.format(hour, minute)
        if flash:
            colon = 255 if seconds & 0x1 else 0
        else:
            colon = 255
        self.write(self.encode_string(string), colon=colon)

