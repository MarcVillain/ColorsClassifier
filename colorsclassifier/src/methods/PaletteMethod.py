from colorthief import ColorThief
from colorsclassifier.src.methods import Method


class PaletteMethod(Method):
    def get_palette(self, image):
        color_thief = ColorThief(image)
        palette = color_thief.get_palette(color_count=self.precision)
        return palette
