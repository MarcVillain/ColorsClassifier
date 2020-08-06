from colorsclassifier.src.outputs import Output

from colorsclassifier.src.helpers.FilesHelper import FilesHelper


class FilenamesOutput(Output):
    """
    Output class.

    The output will be done by copying every image into
    the output folder and prepending its name with the
    sorting value.
    """

    def prepare(self):
        """
        Prepare the output structure, if necessary.
        :return: True on success, else False.
        """
        return FilesHelper.create_dir(self.output_path, self.force)

    def compute(self, classified):
        """
        Build the output using the classification information.
        :param classified: Classification information.
        """
        for name, value in classified.items():
            # Handle colored tile generation
            colored_tile_path = FilesHelper.join(
                self.output_path, name + ".jpg"
            )
            self.gen_colored_tile(colored_tile_path, value.get("rgb"), name)

            for image in value.get("images"):
                # Copy image to new location
                image_name = name + "_" + FilesHelper.basename(image)
                new_image = FilesHelper.join(self.output_path, image_name)
                FilesHelper.copy(image, new_image)
