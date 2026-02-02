import tkinter as tk
from tkinter import ttk

class Student_list_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # self.rowconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        listbox = tk.Listbox(self, font=(None, 30), )
        listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side="right", fill="y")

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command = listbox.yview)

        for i in range(100):
            text = f"Student {i}"
            listbox.insert("end", text)

        listbox.bind('<<ListboxSelect>>', lambda e: print("something"))


