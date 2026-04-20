import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

class Student_grade_counter(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.score_label = ttk.Label(self, text="", font=(None, 20))    
        self.score_label.grid(column=1, row=0)
        ttk.Button(self, text="Confirm\ngrade", width=(0.05*self.container.screen_width),  command=self.confirm).grid(column=0, row=0)

        for widget in self.winfo_children():
            widget.grid(ipadx=10, ipady=10, padx=10)


    def update(self, student):
        self.score_label.config(text=f"{round(student.grade, 1)}/{student.max_grade}") 

    def confirm(self):
        student = self.container.get_selected_student()
        if student:
            student.confirm_grade()
            self.container.update_views(None)
            self.container.top_right_button_frame.autosave()
        else:
            messagebox.showerror("Error", "Please select a student first.")
    




