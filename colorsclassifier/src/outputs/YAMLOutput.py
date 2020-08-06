import yaml

from colorsclassifier.src.helpers.FilesHelper import FilesHelper

from colorsclassifier.src.outputs import Output


class YAMLOutput(Output):
    """
    Output class.

    This output will be done by generating a YAML
    file representing the group of images for each
    classification based on the sorting value.
    """

    def prepare(self):
        """
        Prepare the output structure, if necessary.
        :return: True on success, else False.
        """
        return FilesHelper.create_file(
            self.output_path, "result.yaml", self.force
        )

    def compute(self, classified):
        """
        Build the output using the classification information.
        :param classified: Classification information.
        """
        with open(self.output_path, "w") as output_file:
            yaml.dump(classified, output_file)
