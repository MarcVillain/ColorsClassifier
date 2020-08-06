from colorsclassifier.src.sortings import Sorting


class RGBSorting(Sorting):
    """
    Sorting class.

    The output will be represented by the precisely
    matched RGB value.
    """

    def get_value_for(self, r, g, b):
        """
        Get value representation for sorting.
        :param r: Red value.
        :param g: Blue value.
        :param b: Green value.
        :return: Concatenation of the RGB values.
        """
        return f"{r}-{g}-{b}"
