import logging
from tkinter import messagebox

from src.context import Context


logger = logging.getLogger("color_classifier")


class IOHelper:
    @staticmethod
    def ask_yes_no(message):
        """
        Ask a yes/no question, default being no.
        :param message: The message to display.
        :return: True if input is case insensitive "y" or "yes" else False.
        """
        if Context.is_gui:
            return messagebox.askyesno("Confirmation", message)
        else:
            print(message, "[y/N]", end="")
            choice = input().lower()
            return choice in ["y", "yes"]

    @staticmethod
    def info(message):
        if Context.is_gui:
            messagebox.showinfo("Information", message)
        else:
            logger.info(message)
