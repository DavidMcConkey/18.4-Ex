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
        """Make new generator, beginning at start"""
        self.start = self.next = start

    def __repr__(self):
        """Returns representation of data"""
        return f"<SerialGenerator start= {self.start} next= {self.next}"

    def generate(self):
        """Returns next serial number"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets number back to start"""
        self.next = self.start
