from helpers.FilesHelper import FilesHelper

from methods.AverageMethod import AverageMethod
from methods.DominantMethod import DominantMethod

from sortings.NameSorting import NameSorting
from sortings.RGBSorting import RGBSorting

class Classifier:
    methods = {
        "average": AverageMethod,
        "dominant": DominantMethod,
    }
    sortings = {
        "name": NameSorting,
        "rgb": RGBSorting,
    }

    def __init__(self, precision, method_name="dominant", sort_by="name"):
        self.method = self.methods.get(method_name)(precision)
        self.sorting = self.sortings.get(sort_by)()

    def classify(self, folder):
        """
        :return: Dictionnary of classified images.
        """
        output = {}
        for image in FilesHelper.get_images_in(folder):
            palette = self.method.get_palette(image)
            for r, g, b in palette:
                sort_value = self.sorting.get_value_for(r, g, b)
                # Make sure the list is set
                output[sort_value] = output.get(sort_value, [])
                # Append image to the list
                output[sort_value].append(image)
        return output
