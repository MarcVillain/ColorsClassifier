import logging

from src.config import Config
from src.helpers.FilesHelper import FilesHelper

logger = logging.getLogger("color_classifier")


class Classifier:
    def __init__(
        self,
        precision,
        method_name=Config.default_method,
        sort_by=Config.default_sorting,
    ):
        self.method = Config.methods.get(method_name)(precision)
        self.sorting = Config.sortings.get(sort_by)()

    def classify(self, folder, recurse=False):
        """
        :return: Dictionary of classified images.
        """
        output = {}
        images = FilesHelper.get_images_in(folder, recurse=recurse)
        images_len = len(images)

        for i, image in enumerate(images):
            image_count = i + 1
            logger.info(f"Computing image ({image_count}/{images_len})")
            palette = self.method.get_palette(image)
            for r, g, b in palette:
                sort_value = self.sorting.get_value_for(r, g, b)
                # Make sure the element exists
                output[sort_value] = output.get(
                    sort_value, {"rgb": (r, g, b), "images": []}
                )
                # Append image to the list
                output[sort_value]["images"].append(image)
        return output
