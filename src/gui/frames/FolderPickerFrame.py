import tkinter as tk
from tkinter import ttk, filedialog


class FolderPickerFrame(tk.Frame):
    def __init__(self, title, command, master=None):
        super().__init__(master=master)

        self.command = command

        title = tk.Label(self, text=title)
        title.grid(row=0, column=0, pady=5, padx=5)
        self.label = tk.Label(self, text="")
        self.label.grid(row=0, column=1, pady=5, padx=5)
        button = ttk.Button(self, text="Browse", command=self.file_dialog)
        button.grid(row=0, column=2, pady=5, padx=5)

    def file_dialog(self):
        folder_path = filedialog.askdirectory(
            initialdir=".", title="Select the output folder"
        )
        self.command(folder_path)
        self.label.configure(text=folder_path)
