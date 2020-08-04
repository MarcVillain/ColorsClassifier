import tkinter as tk
from tkinter import ttk

from src import run
from src.gui.frames.FolderPickerFrame import FolderPickerFrame
from src.gui.frames.MethodFrame import MethodFrame
from src.gui.frames.OutputFrame import OutputFrame
from src.gui.frames.SortingFrame import SortingFrame


class MainWindow(tk.Tk):
    def __init__(self, args):
        super().__init__()

        self.args = args

        self.geometry("500x400")
        self.title("Colors Classifier")

        def _set_images_folder(value):
            self.args.images_folder = value

        FolderPickerFrame(
            "Images folder:", _set_images_folder, master=self
        ).grid(row=0, column=0, pady=5, padx=5)

        def _set_output(value):
            self.args.output = value

        FolderPickerFrame("Output folder:", _set_output, master=self).grid(
            row=1, column=0, pady=5, padx=5
        )

        MethodFrame(self, master=self).grid(row=2, column=0, pady=5, padx=5)
        OutputFrame(self, master=self).grid(row=3, column=0, pady=5, padx=5)
        SortingFrame(self, master=self).grid(row=4, column=0, pady=5, padx=5)

        output_color_var = tk.IntVar(
            value=(1 if self.args.output_color else 0)
        )

        def _set_output_color():
            self.args.output_color = not self.args.output_color

        tk.Label(self, text="Output colored tile?").grid(
            row=5, column=0, pady=5, padx=5
        )
        ttk.Checkbutton(
            self, variable=output_color_var, command=_set_output_color
        ).grid(row=5, column=1, pady=5, padx=5)

        def _run():
            run(args)

        button = ttk.Button(self, text="Classify", command=_run)
        button.grid(row=10, column=0, columnspan=2, pady=5)
