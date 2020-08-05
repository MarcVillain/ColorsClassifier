import yaml

from colorsclassifier.src.helpers.FilesHelper import FilesHelper

from colorsclassifier.src.outputs import Output


class YAMLOutput(Output):
    def prepare(self):
        return FilesHelper.create_file(
            self.output_path, "result.yaml", self.force
        )

    def compute(self, classified):
        with open(self.output_path, "w") as output_file:
            yaml.dump(classified, output_file)