import tkinter as tk
from tkinter import ttk, filedialog

class Top_left_buttons_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # self.rowconfigure(0, weight=1)
        self.container = container

        ttk.Button(self, text="select folder", width=20, command=self.load_folder).grid(column=0, row=0)
        ttk.Button(self, text="select reubrics", width=20).grid(column=1, row=0)
        ttk.Button(self, text="autograde", width=20).grid(column=2, row=0)

        for widget in self.winfo_children():
            widget.grid(ipadx=20, ipady=20, padx=20)
        

    def load_folder(self):
        self.container.load_folder()
