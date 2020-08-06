from abc import ABC


class Method(ABC):
    """
    Method abstract class.
    """

    def __init__(self, precision=6):
        """
        Initialize class.
        :param precision: Precision value used for PaletteMethod.
        """
        self.precision = precision

    def get_palette(self, image):
        """
        Compute list of colors extracted form the image.
        :param image: Path to the image to manipulate.
        :return: List of RGB tuples.
        """
        pass
