import tkinter as tk
from tkinter import ttk, filedialog

class Top_left_buttons_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # self.rowconfigure(0, weight=1)
        self.container = container

        ttk.Button(self, text="select folder", width=(0.05*self.container.winfo_screenwidth()), command=self.load_folder).grid(column=0, row=0)
        ttk.Button(self, text="select rubrics", width=(0.05*self.container.winfo_screenwidth()), command=self.load_rubrics).grid(column=1, row=0)
        ttk.Button(self, text="autograde", width=(0.05*self.container.winfo_screenwidth()), command=self.poop).grid(column=2, row=0)

        for widget in self.winfo_children():
            widget.grid(ipadx=10, ipady=10, padx=10)
        

    def load_folder(self):
        self.container.load_folder()
    
    def load_rubrics(self):
        self.container.load_rubrics()
    

    def poop(self):
        print(self.container.current_student.name)
        print(self.container.students)
