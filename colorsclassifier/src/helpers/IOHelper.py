import logging

import tkinter as tk
from tkinter import messagebox

from colorsclassifier.src.context import Context


logger = logging.getLogger("color_classifier")


class IOHelper:
    """
    Helper class.

    Helps to handle input and output with user.
    """

    @staticmethod
    def ask_yes_no(message):
        """
        Ask a yes/no question, default being no.
        :param message: The message to display.
        :return: True if input is case insensitive "y" or "yes" else False.
        """
        if Context.is_gui:
            res = (
                messagebox.askquestion(
                    "Confirmation", message, icon="warning"
                )
                == "yes"
            )
            # Due to a weird bug in MacOS when using Tkinter,
            # the messagebox will not close immediately and we
            # need to get focus back to the main window manually
            # to at least make it seem like its intended.
            tk._default_root.grab_set()
            tk._default_root.grab_release()
            return res
        else:
            print(message, "[y/N]", end="")
            choice = input().lower()
            return choice in ["y", "yes"]
