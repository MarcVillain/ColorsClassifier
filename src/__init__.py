import logging

from src.classifier import Classifier
from src.config import Config
from src.helpers.IOHelper import IOHelper

logger = logging.getLogger()


def run(args):
    print(args)
    output_type = Config.output_types.get(
        args.output_type, Config.output_types.get(Config.default_output)
    )
    output = output_type(args.output, args.output_color, args.force)

    if output.prepare():
        classifier = Classifier(args.precision, args.method, args.sort_by)
        classified = classifier.classify(args.images_folder, args.recurse)
        output.compute(classified)
        IOHelper.info(f"Output available at {args.output}")
