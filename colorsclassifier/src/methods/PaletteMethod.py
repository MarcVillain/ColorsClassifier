from colorthief import ColorThief
from colorsclassifier.src.methods import Method


class PaletteMethod(Method):
    """
    Method class.

    The method used is the extraction of a palette of
    the dominant colors.

    This has a better precision since the most important
    elements to extract are usually in the top of this
    list, allowing for precise but still broad search of
    the image colors.

    The precision can be tweaked by changing the amount
    of extracted colors.
    """

    def get_palette(self, image):
        """
        Compute list of colors extracted form the image.
        :param image: Path to the image to manipulate.
        :return: List of RGB tuples.
        """
        color_thief = ColorThief(image)
        palette = color_thief.get_palette(color_count=self.precision)
        return palette
