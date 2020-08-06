from colorsclassifier.src.outputs import Output

from colorsclassifier.src.helpers.FilesHelper import FilesHelper


class FoldersOutput(Output):
    """
    Output class.

    The output will be done by copying every image into
    a folder created in the output folder. This folder
    will be named using the sorting value.
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
            # Create destination directory
            new_dir = FilesHelper.join(self.output_path, name)
            FilesHelper.create_dir(new_dir, ignore_errors=True)

            # Handle colored tile generation
            colored_tile_path = FilesHelper.join(new_dir, name + ".jpg")
            self.gen_colored_tile(colored_tile_path, value.get("rgb"), name)

            # Copy images to new directory
            for image in value.get("images"):
                image_name = FilesHelper.basename(image)
                new_image = FilesHelper.join(new_dir, image_name)
                FilesHelper.copy(image, new_image)
