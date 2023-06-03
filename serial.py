"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """create a variable to store the current serial number- default - start=0"""
        self.current = start

    def generate(self):
        """Increment the current serial number by 1 and return it"""
        serial_number = self.current
        self.current += 1
        return serial_number

    def reset(self):
        """Set the current current serial number back to the starting value = 0"""
        self.current = 0
