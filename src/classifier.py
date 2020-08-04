import logging

from src.helpers.FilesHelper import FilesHelper

from src.methods.AverageMethod import AverageMethod
from src.methods.DominantMethod import DominantMethod
from src.methods.PaletteMethod import PaletteMethod

from src.sortings.NameSorting import NameSorting
from src.sortings.RGBSorting import RGBSorting

logger = logging.getLogger()


class Classifier:
    methods = {
        "average": AverageMethod,
        "dominant": DominantMethod,
        "palette": PaletteMethod,
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
        images = FilesHelper.get_images_in(folder)
        images_len = len(images)

        for i, image in enumerate(images):
            image_count = i + 1
            logger.info(f"Computing image ({image_count}/{images_len})")
            palette = self.method.get_palette(image)
            for r, g, b in palette:
                sort_value = self.sorting.get_value_for(r, g, b)
                # Make sure the list is set
                output[sort_value] = output.get(sort_value, [])
                # Append image to the list
                output[sort_value].append(image)
        return output
