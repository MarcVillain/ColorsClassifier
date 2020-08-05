from colorsclassifier.src.outputs import Output

from colorsclassifier.src.helpers.FilesHelper import FilesHelper


class FilenamesOutput(Output):
    def prepare(self):
        return FilesHelper.create_dir(self.output_path, self.force)

    def compute(self, classified):
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
