from src.outputs import Output

from src.helpers.FilesHelper import FilesHelper


class FoldersOutput(Output):
    def prepare(self):
        return FilesHelper.create_dir(self.output_path, self.force)

    def compute(self, classified):
        for name, images in classified.items():
            # Create destination directory
            new_dir = FilesHelper.join(self.output_path, name)
            FilesHelper.create_dir(new_dir, ignore_errors=True)
            for image in images:
                # Copy image to new directory
                image_name = FilesHelper.basename(image)
                new_image = FilesHelper.join(new_dir, image_name)
                FilesHelper.copy(image, new_image)
