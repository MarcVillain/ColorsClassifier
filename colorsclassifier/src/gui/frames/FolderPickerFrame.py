import tkinter as tk
from tkinter import ttk, filedialog


class FolderPickerFrame(tk.Frame):
    """
    Tkinter Frame class.
    """

    def __init__(self, title, command, master=None):
        """
        Initialize class.
        :param title: Title of the directory dialog box.
        :param command: Command to run on the selected path.
        :param master: Parent Tkinter element.
        """
        super().__init__(master=master)

        self.title = title
        self.command = command

        sv = tk.StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.command(sv.get()))
        self.entry = tk.Entry(self, textvariable=sv)
        self.entry.configure(width=20)
        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        button = ttk.Button(self, text="Browse", command=self.file_dialog)
        button.configure(width=10)
        button.pack(side=tk.LEFT)

    def file_dialog(self):
        """
        Handle 'Browse' button press.
        """
        folder_path = filedialog.askdirectory(
            initialdir=".", title=self.title
        )
        self.command(folder_path)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, folder_path)
