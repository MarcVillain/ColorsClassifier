import multiprocessing
import tkinter as tk
from multiprocessing.context import Process
from tkinter import ttk

from PIL import Image, ImageTk

from colorsclassifier.src import run
from colorsclassifier.src.context import Context
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

        self.title("ColorsClassifier")
        self.configure(background="white")

        # Set background image
        image = Image.open(f"{Context.app_images_folder}/background.png")
        self.background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1)

        # Set size of empty rows and columns
        self.grid_rowconfigure(0, minsize=100)
        self.grid_rowconfigure(9, minsize=20)
        self.grid_columnconfigure(0, minsize=40)
        self.grid_columnconfigure(3, minsize=40)

        # Set button
        self.button = ttk.Button(
            self, text="Classify", command=self._on_click
        )
        self.button.grid(
            sticky="nesw", row=7, column=1, columnspan=2, pady=5, padx=5
        )

        # Set labels
        def _set_label(text, row):
            label = tk.Label(text=text, anchor="w")
            label.configure(width=15)
            label.grid(sticky="w", row=row, column=1, pady=5, padx=5)

        _set_label("Images folder", 1)
        _set_label("Method", 2)
        _set_label("Output", 3)
        _set_label("Sorting", 4)
        _set_label("Output colored tile?", 5)
        _set_label("Output folder", 6)

        # Set elements
        def _set_images_folder(value):
            self.args.images_folder = value
            # TODO: Check for enabling button

        FolderPickerFrame(
            "Select images folder", _set_images_folder, master=self
        ).grid(sticky="w", row=1, column=2, pady=5, padx=5)

        def _set_output(value):
            self.args.output = value
            # TODO: Check for enabling button

        FolderPickerFrame(
            "Select output folder", _set_output, master=self
        ).grid(sticky="w", row=6, column=2, pady=5, padx=5)

        MethodFrame(self, master=self).grid(
            sticky="w", row=2, column=2, pady=5, padx=5
        )
        OutputFrame(self, master=self).grid(
            sticky="w", row=3, column=2, pady=5, padx=5
        )
        SortingFrame(self, master=self).grid(
            sticky="w", row=4, column=2, pady=5, padx=5
        )

        output_color_var = tk.IntVar(
            value=(1 if self.args.output_color else 0)
        )

        def _set_output_color():
            self.args.output_color = not self.args.output_color

        # FIXME: Check button "-" state is confusing
        ttk.Checkbutton(
            self, variable=output_color_var, command=_set_output_color
        ).grid(sticky="w", row=5, column=2, pady=5, padx=5)

        # Set info bar
        self.info_label = tk.Label(self, text="")
        self.info_label.configure(background="white", foreground="black")
        self.info_label.grid(row=8, column=1, columnspan=2, pady=5, padx=5)

    def _on_click(self):
        self.button.config(state=tk.DISABLED)
        self.p1 = Process(
            target=run, args=(self.args, self.queue, Context.serialize(),)
        )
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
