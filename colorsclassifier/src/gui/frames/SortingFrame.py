import logging

from colorsclassifier.src.config import Config
from colorsclassifier.src.gui.frames.OptionFrame import OptionFrame


logger = logging.getLogger("color_classifier")


class SortingFrame(OptionFrame):
    """
    OptionFrame class.
    """

    def __init__(self, main_window, master=None):
        """
        Initialize class.
        :param main_window: MainWindow instance.
        :param master: Parent Tkinter element.
        """
        def _set_sorting(value):
            logger.debug(f"Set sorting to '{value}'.")
            main_window.args.sort_by = value

        super().__init__(
            default_value=Config.default_sorting,
            values=Config.sortings,
            command=_set_sorting,
            master=master,
        )
