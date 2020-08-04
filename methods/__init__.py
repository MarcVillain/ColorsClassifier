from abc import ABC


class Method(ABC):
    def __init__(self, precision=6):
        self.precision = precision

    def get_palette(self, image):
        """
        :return: List of RGB tuples.
        """
        pass
