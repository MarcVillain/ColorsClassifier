import logging

from src.config import Config
from src.gui.frames.OptionFrame import OptionFrame


logger = logging.getLogger()


class OutputFrame(OptionFrame):
    def __init__(self, main_window, master=None):
        def _set_output(value):
            logger.debug(f"Set output to '{value}'.")
            main_window.args.output_type = value

        super().__init__(
            default_value=Config.default_output,
            values=Config.output_types,
            command=_set_output,
            title="Output",
            master=master,
        )
