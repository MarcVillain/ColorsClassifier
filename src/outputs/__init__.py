import logging

from abc import ABC

from PIL import Image, ImageDraw, ImageFont

from src.sortings.NameSorting import NameSorting

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

    def gen_colored_tile(self, file_path, rgb, name=None):
        if self.output_color:
            rgb = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
            colored_tile = Image.new("RGB", (50, 50), rgb)
            draw = ImageDraw.Draw(colored_tile)

            # Add informative text
            draw.text(
                (0, 0),
                "Detected",
                font=ImageFont.truetype("Arial"),
                fill=(255, 255, 255),
                stroke_fill=(0, 0, 0),
                stroke_width=1,
            )

            if name is not None:
                # Add real color to square
                draw.rectangle(
                    ((0, 25), (50, 50)), fill=NameSorting.colors.get(name)
                )
                # Add informative text
                draw.text(
                    (0, 25),
                    "Closest",
                    font=ImageFont.truetype("Arial"),
                    fill=(255, 255, 255),
                    stroke_fill=(0, 0, 0),
                    stroke_width=1,
                )

            colored_tile.save(file_path)
