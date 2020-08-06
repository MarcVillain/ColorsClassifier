import logging
import tkinter as tk
from tkinter import ttk

logger = logging.getLogger("color_classifier")


class OptionFrame(tk.Frame):
    """
    Tkinter Frame class.
    """

    def __init__(self, default_value, values, command, master=None):
        """
        Initialize class.
        :param default_value: Default option selected.
        :param values: Dictionary of name/value elements.
        :param command: Command to run on the selected value.
        :param master: Parent Tkinter element.
        """
        super().__init__(master=master)

        var = tk.StringVar(self)
        var.set(default_value)

        option_menu = ttk.OptionMenu(
            self, var, default_value, *values, command=command,
        )
        option_menu.config(width=30)
        option_menu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
