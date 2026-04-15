import tkinter as tk
from tkinter import ttk
import csv


class Top_right_buttons_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container 
        ttk.Button(self, text="Export csv", width=(0.05*self.container.screen_width), command=self.export_csv).grid(column=1, row=0)

        for widget in self.winfo_children():
            widget.grid(ipadx=10, ipady=10, padx=10)


    def export_csv(self):
        firstLine = 'Last name,First name,ANR,'
        for q in self.container.questions.values():
            firstLine += f'{q.id},Rubrics,'
        firstLine+='Total'

        with open("results.csv", "w") as csvfile:
            csvfile.write(firstLine+'\n')
            for student in self.container.students.values():
                student_record = student.get_record()
                csvfile.write(student_record+'\n')



        
        
    

        
