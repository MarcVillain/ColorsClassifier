import cv2
import numpy

from colorsclassifier.src.methods import Method


class AverageMethod(Method):
    """
    Method class.

    The method used is the overall average of the image.

    This is a not very precise method, but it has its
    use cases.
    """

    def get_palette(self, image):
        """
        Compute list of colors extracted form the image.
        :param image: Path to the image to manipulate.
        :return: List of RGB tuples.
        """
        img = cv2.imread(image)
        avg_color_per_row = numpy.average(img, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
        return [avg_color]
