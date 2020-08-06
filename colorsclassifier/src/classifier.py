import logging

from colorsclassifier.src.config import Config
from colorsclassifier.src.helpers.FilesHelper import FilesHelper

logger = logging.getLogger("color_classifier")


class Classifier:
    def __init__(
        self,
        precision,
        method_name=Config.default_method,
        sort_by=Config.default_sorting,
        message_queue=None,
    ):
        """
        Initialize class.
        :param precision: Precision value used for PaletteMethod.
        :param method_name: Name of the method (aka algorithm) to use.
        :param sort_by: Name of the sort operation to use.
        :param message_queue: Used when started in another process to retrieve messages.
        """
        self.method = Config.methods.get(method_name)(precision)
        self.sorting = Config.sortings.get(sort_by)()
        self.message_queue = message_queue

    def classify(self, folder, recurse=False):
        """
        Call classification operation on every image.
        :param folder: Folder where the images to classify are.
        :param recurse: If true, look also for images in subdirectories.
        :return: Dictionary of classified images.
        """
        output = {}
        images = FilesHelper.get_images_in(folder, recurse=recurse)
        images_len = len(images)

        for i, image in enumerate(images):
            image_count = i + 1

            message = f"Computing image ({image_count}/{images_len})"
            if self.message_queue is not None:
                self.message_queue.put(message)
            logger.info(message)

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
