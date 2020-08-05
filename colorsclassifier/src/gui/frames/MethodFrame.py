import logging

from colorsclassifier.src.config import Config
from colorsclassifier.src.gui.frames.OptionFrame import OptionFrame


logger = logging.getLogger("color_classifier")


class MethodFrame(OptionFrame):
    def __init__(self, main_window, master=None):
        def _set_method(value):
            logger.debug(f"Set method to '{value}'.")
            main_window.args.method = value

        super().__init__(
            default_value=Config.default_method,
            values=Config.methods,
            command=_set_method,
            title="Method",
            master=master,
        )
