import logging

from colorsclassifier.src.classifier import Classifier
from colorsclassifier.src.config import Config
from colorsclassifier.src.context import Context

logger = logging.getLogger("color_classifier")


def run(args, message_queue=None, context=None):
    """
    Run the classification computation.
    :param args:
    :param message_queue: Used when started in another process to retrieve messages.
    :param context: Used when started in another process to retrieve context data.
    :return:
    """
    if context is not None:
        Context.deserialize(context)

    output_type = Config.output_types.get(
        args.output_type, Config.output_types.get(Config.default_output)
    )
    output = output_type(args.output, args.output_color, args.force)

    if output.prepare():
        classifier = Classifier(
            args.precision, args.method, args.sort_by, message_queue
        )
        classified = classifier.classify(args.images_folder, args.recurse)
        output.compute(classified)

        message = f"Output available at {args.output}"
        if message_queue is not None:
            message_queue.put(message)
        logger.info(message)
