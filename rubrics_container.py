import tkinter as tk
from tkinter import ttk
from rubrics import *

class Rubrics_box(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.__create_widget()
    

        
    
    def __create_widget(self):
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure((1,2,3,4,5), weight=10)
        frame.pack(ipadx=10, ipady=1, expand=False)
        
        rubric_1 = Rubrics(frame, "rubrics 1", "is even")
        rubric_1.focus()
        rubric_1.grid(row=1, column=0)

        rubric_2 = Rubrics(frame, "rubrics 2", "return integer")
        rubric_2.focus()
        rubric_2.grid(row=4, column=0)
        


