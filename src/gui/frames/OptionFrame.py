import logging
import tkinter as tk
from tkinter import ttk

logger = logging.getLogger("color_classifier")


class OptionFrame(tk.Frame):
    def __init__(self, default_value, values, command, title, master=None):
        super().__init__(master=master)

        var = tk.StringVar(self)
        var.set(default_value)

        tk.Label(self, text=f"{title}: ").grid(row=0, column=0)
        ttk.OptionMenu(
            self, var, default_value, *values, command=command,
        ).grid(row=0, column=1)
