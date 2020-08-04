import cv2
import numpy

from src.methods import Method


class AverageMethod(Method):
    def get_palette(self, image):
        img = cv2.imread(image)
        avg_color_per_row = numpy.average(img, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
        return [avg_color]
