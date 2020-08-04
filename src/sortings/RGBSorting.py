from src.sortings import Sorting

class RGBSorting(Sorting):
    def get_value_for(self, r, g, b):
        return f"{r}-{g}-{b}"
