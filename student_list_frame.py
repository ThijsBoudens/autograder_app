import tkinter as tk
from tkinter import ttk
from center_text_box import *
import os

class Student_list_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # self.rowconfigure(0, weight=1)
        self.listbox = tk.Listbox(self, font=(None, 30), )
        self.listbox.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command = self.listbox.yview)

        self.container = container

    def list_folder_content(self, folder_path):
        files = os.listdir(folder_path)
        for file in files:
            if file[-3:] == ".py":
                self.listbox.insert("end", file)
        self.listbox.bind('<<ListboxSelect>>', lambda e: self.get_file_content(folder_path))


    def get_file_content(self, folder):
        selected_indice = self.listbox.curselection()
        selected_file_path = folder+"/"+self.listbox.get(selected_indice)
        with open(selected_file_path, 'r') as f:
            content = f.read()
            self.container.textbox.set_text(content)

