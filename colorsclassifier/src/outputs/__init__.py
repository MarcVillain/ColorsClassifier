import logging

from abc import ABC

from PIL import Image, ImageDraw, ImageFont

from colorsclassifier.src.sortings.NameSorting import NameSorting

logger = logging.getLogger("color_classifier")


class Output(ABC):
    """
    Output abstract class.
    """

    def __init__(self, output_path, output_color=False, force=False):
        """
        Initialize class.
        :param output_path: Path of output folder.
        :param output_color: If True, add a colored tile to the output.
        :param force: If True, delete the output folder without mercy.
        """
        self.output_path = output_path
        self.output_color = output_color
        self.force = force

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
        pass

    def gen_colored_tile(self, file_path, rgb, name=None):
        """
        Generate a colored tile.
        :param file_path: Location of the file to create.
        :param rgb: Color to put in the image.
        :param name: If set, represents the closest NameSorting color.
        """
        if self.output_color:
            # Build the colored image
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

            # Save the image
            colored_tile.save(file_path)
