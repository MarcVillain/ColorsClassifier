from colorthief import ColorThief
from src.methods import Method


class DominantMethod(Method):
    def get_palette(self, image):
        color_thief = ColorThief(image)
        dominant_color = color_thief.get_color(quality=1)
        return [dominant_color]
