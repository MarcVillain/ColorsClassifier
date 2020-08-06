from colorsclassifier.src.outputs import Output


class StdoutOutput(Output):
    """
    Output class.

    This output will be done by dumping the dictionary
    information directly into the console stdout.
    """

    def prepare(self):
        """
        Prepare the output structure, if necessary.
        """
        pass

    def compute(self, classified):
        """
        Build the output using the classification information.
        :param classified: Classification information.
        """
        print(classified)
