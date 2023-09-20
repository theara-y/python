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
    def __init__(self, start):
        self.start = start
        self.counter = start

    def __repr__(self):
        """ print(repr(SerialGenerator(100))) """
        return f"<SerialGenerator start={self.start} next={self.counter}>"

    def generate(self):
        """ Generates the next number and increments the counter """
        current = self.counter
        self.counter += 1
        return current

    def reset(self):
        """ Resets the counter to the initial number used to create the generator """
        self.counter = self.start