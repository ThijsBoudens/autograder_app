import tkinter as tk
from tkinter import ttk, filedialog

class Top_left_buttons_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # self.rowconfigure(0, weight=1)
        self.container = container

        ttk.Button(self, text="select\nexams folder", width=(0.05*self.container.screen_width), command=self.load_exams).grid(column=0, row=0)
        ttk.Button(self, text="select\nrubrics file", width=(0.05*self.container.screen_width), command=self.load_rubrics).grid(column=1, row=0)
        ttk.Button(self, text="autograde", width=(0.05*self.container.screen_width)).grid(column=2, row=0)

        for widget in self.winfo_children():
            widget.grid(ipadx=10, ipady=10, padx=10)
        

    def load_exams(self):
        self.container.listbox.load_students()
    
    def load_rubrics(self):
        self.container.questions_frame.load_rubrics()
    


