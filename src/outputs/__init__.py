import logging

from abc import ABC

from PIL import Image

logger = logging.getLogger()


class Output(ABC):
    def __init__(self, output_path, output_color=False, force=False):
        self.output_path = output_path
        self.output_color = output_color
        self.force = force

    def prepare(self):
        pass

    def compute(self, classified):
        pass

    def gen_colored_tile(self, file_path, rgb):
        if self.output_color:
            rgb = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
            colored_tile = Image.new("RGB", (1, 1), rgb)
            colored_tile.save(file_path)
