from src.outputs import Output

from src.helpers.FilesHelper import FilesHelper


class FilenamesOutput(Output):
    def prepare(self):
        return FilesHelper.create_dir(self.output_path, self.force)

    def compute(self, classified):
        for name, images in classified.items():
            for image in images:
                # Copy image to new location
                image_name = name + "_" + FilesHelper.basename(image)
                new_image = FilesHelper.join(self.output_path, image_name)
                FilesHelper.copy(image, new_image)
