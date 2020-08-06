from colorthief import ColorThief
from colorsclassifier.src.methods import Method


class DominantMethod(Method):
    """
    Method class.

    The method used is the dominant color of the image.

    This has a good precision but can still be off if
    the image has a lot of the same color as background,
    like for sky or text on a white canvas.
    """

    def get_palette(self, image):
        """
        Compute list of colors extracted form the image.
        :param image: Path to the image to manipulate.
        :return: List of RGB tuples.
        """
        color_thief = ColorThief(image)
        dominant_color = color_thief.get_color(quality=1)
        return [dominant_color]
