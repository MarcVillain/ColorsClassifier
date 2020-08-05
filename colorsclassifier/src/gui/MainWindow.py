import multiprocessing
import tkinter as tk
from multiprocessing.context import Process
from tkinter import ttk

from colorsclassifier.src import run
from colorsclassifier.src.gui.frames.FolderPickerFrame import (
    FolderPickerFrame,
)
from colorsclassifier.src.gui.frames.MethodFrame import MethodFrame
from colorsclassifier.src.gui.frames.OutputFrame import OutputFrame
from colorsclassifier.src.gui.frames.SortingFrame import SortingFrame


class MainWindow(tk.Tk):
    def __init__(self, args):
        super().__init__()

        self.args = args
        self.queue = multiprocessing.Queue()

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

        self.info_label = tk.Label(self, text="")

        self.button = ttk.Button(
            self, text="Classify", command=self._on_click
        )
        self.button.grid(row=10, column=0, columnspan=2, pady=5)

        self.info_label.grid(row=11, column=0, columnspan=2, pady=5, padx=5)

    def _on_click(self):
        self.button.config(state=tk.DISABLED)
        self.p1 = Process(target=run, args=(self.args, self.queue,))
        self.p1.start()
        self.after(100, self._on_update)

    def _on_update(self):
        while not self.queue.empty():
            message = self.queue.get()
            self.info_label.configure(text=message)

        if self.p1.is_alive():
            self.after(100, self._on_update)
            return
        self.button.config(state=tk.NORMAL)
