import argparse
import logging
import sys

from colorsclassifier.src import run
from colorsclassifier.src.config import Config
from colorsclassifier.src.context import Context
from colorsclassifier.src.gui import center
from colorsclassifier.src.gui.MainWindow import MainWindow

logger = logging.getLogger("color_classifier")
logger.setLevel(logging.INFO)
logger_formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
)
logger_console_stream = logging.StreamHandler(sys.stdout)
logger_console_stream.setFormatter(logger_formatter)
logger_console_stream.setLevel(logging.INFO)
logger.addHandler(logger_console_stream)


def parse_command_line():
    """
    Parse the command line.
    :return: Dictionnary of arguments.
    """
    parser = argparse.ArgumentParser(
        description="""
        Simple script that lets you order images based on color.
        """,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # Arguments
    parser.add_argument(
        "-i",
        "--images-folder",
        metavar="FOLDER",
        help="Folder where all images to classify are located.",
    )

    # Options
    parser.add_argument(
        "--debug", help="Display debug information.", action="store_true"
    )

    parser.add_argument(
        "-o",
        "--output",
        metavar="FOLDER",
        help="Output folder.",
        default="output",
    )

    parser.add_argument(
        "-t",
        "--output-type",
        metavar="TYPE",
        help="Type of output to use. Allowed values are "
        + ", ".join(Config.output_types)
        + ".",
        choices=Config.output_types,
        default=Config.default_output,
    )

    parser.add_argument(
        "-c",
        "--output-color",
        help="Output a colored tile to have a visual cue of the color.",
        action="store_true",
    )

    parser.add_argument(
        "-m",
        "--method",
        metavar="NAME",
        help="Method to use for classification. Allowed values are "
        + ", ".join(Config.methods.keys())
        + ".",
        choices=Config.methods.keys(),
        type=str,
        default=Config.default_method,
    )

    parser.add_argument(
        "-p",
        "--precision",
        metavar="COLORS_COUNT",
        help="Number of colors to extract in a palette for each image.",
        type=int,
        default=6,
    )

    parser.add_argument(
        "-s",
        "--sort-by",
        metavar="TYPE",
        help="Type of sorting to use. Allowed values are "
        + ", ".join(Config.sortings.keys())
        + ".",
        choices=Config.sortings.keys(),
        type=str,
        default=Config.default_sorting,
    )

    parser.add_argument(
        "-r",
        "--recurse",
        help="Look for images in subdirectories as well.",
        action="store_true",
    )

    parser.add_argument(
        "-f",
        "--force",
        help="Do not ask for confirmation to override files or folders. Use cautiously.",
        action="store_true",
    )

    parser.add_argument(
        "-g",
        "--gui",
        help="Start GUI instead of using command line.",
        action="store_true",
    )

    return parser.parse_args()


def main():
    args = parse_command_line()

    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger_console_stream.setLevel(logging.DEBUG)
    logger.debug(f"Program arguments: {args}")

    Context.is_gui = args.gui

    if Context.is_gui:
        window = MainWindow(args)
        center(window)
        window.mainloop()
    else:
        run(args)


if __name__ == "__main__":
    main()
