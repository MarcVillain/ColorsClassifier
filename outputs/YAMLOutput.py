import yaml

from helpers.FilesHelper import FilesHelper

from outputs import Output

class YAMLOutput(Output):
    def prepare(self):
        return FilesHelper.create_file(self.output_path, self.force)

    def compute(self, classified):
        with open(self.output_path, "w") as output_file:
            yaml_format = yaml.dump(classified, output_file)
