import logging

from src.config import Config
from src.gui.frames.OptionFrame import OptionFrame


logger = logging.getLogger("color_classifier")


class SortingFrame(OptionFrame):
    def __init__(self, main_window, master=None):
        def _set_sorting(value):
            logger.debug(f"Set sorting to '{value}'.")
            main_window.args.sort_by = value

        super().__init__(
            default_value=Config.default_sorting,
            values=Config.sortings,
            command=_set_sorting,
            title="Sorting",
            master=master,
        )
