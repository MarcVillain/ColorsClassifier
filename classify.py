import argparse
import logging
import sys

from src.classifier import Classifier
from src.outputs.FilenamesOutput import FilenamesOutput
from src.outputs.FoldersOutput import FoldersOutput
from src.outputs.StdoutOutput import StdoutOutput
from src.outputs.YAMLOutput import YAMLOutput

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger_formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
)
logger_console_stream = logging.StreamHandler(sys.stdout)
logger_console_stream.setFormatter(logger_formatter)
logger_console_stream.setLevel(logging.INFO)
logger.addHandler(logger_console_stream)


default_output = "yaml"
output_types = {
    "yaml": YAMLOutput,
    "filenames": FilenamesOutput,
    "folders": FoldersOutput,
    "stdout": StdoutOutput,
}


def main(args):
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger_console_stream.setLevel(logging.DEBUG)

    logger.debug(f"Program arguments: {args}")

    output_type = output_types.get(
        args.output_type, output_types.get(default_output)
    )
    output = output_type(args.output, args.output_color, args.force)

    if output.prepare():
        classifier = Classifier(args.precision, args.method, args.sort_by)
        classified = classifier.classify(args.folder)
        logger.info(f"Creating output at {args.output}")
        output.compute(classified)


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
        "folder",
        metavar="IMAGES_FOLDER",
        help="Folder where all images are located.",
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
        + ", ".join(output_types)
        + ".",
        choices=output_types,
        default=default_output,
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
        + ", ".join(Classifier.methods.keys())
        + ".",
        choices=Classifier.methods.keys(),
        type=str,
        default=Classifier.default_method,
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
        + ", ".join(Classifier.sortings.keys())
        + ".",
        choices=Classifier.sortings.keys(),
        type=str,
        default=Classifier.default_sorting,
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

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_command_line()
    main(args)
