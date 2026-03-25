import tkinter as tk 
from tkinter import ttk

class Student_grade_counter(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.score_label = ttk.Label(self.container, text="", font=(None, 20), compound=tk.CENTER)    
        self.score_label.grid(column=1, row=0)


    def update(self, student):
        self.score_label.config(text=f"{round(student.grade, 1)}/{student.max_grade}") 
    




