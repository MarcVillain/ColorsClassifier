import argparse
import logging

logger = logging.getLogger()

def main(args):
    print("Hello, World!")


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
        "-m",
        "--method",
        metavar="NAME",
        help="Method to use for classification",
        choices=("average", "dominant"),
        type=str,
        default="dominant"
    )

    parser.add_argument(
        "-p",
        "--precision",
        metavar="COLORS_COUNT",
        help="Number of colors to extract in a palette for each image.",
        type=int,
        default=6,
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_command_line()
    main(args)
