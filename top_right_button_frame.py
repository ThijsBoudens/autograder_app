import tkinter as tk
from tkinter import ttk
import csv


class Top_right_buttons_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container 
        ttk.Button(self, text="Set scores", width=(0.05*self.container.screen_width), command=self.set_results).grid(column=0, row=0)
        ttk.Button(self, text="Export csv", width=(0.05*self.container.screen_width), command=self.export_csv).grid(column=1, row=0)

        for widget in self.winfo_children():
            widget.grid(ipadx=10, ipady=10, padx=10)

    
    def set_results(self):
        self.container.set_results()


    def export_csv(self):
        if self.container.students:
            with open("file.csv", "w", newline='') as csvfile:
                field_names = ["student_names"]
                for question in self.container.questions:
                    field_names.append(question)
                    field_names.append(f"rubrics_{question}")
                field_names.append("total_score")
                writer = csv.writer(csvfile)
                writer.writerow(field_names)
                
                for student in self.container.students.values():
                    if student.been_graded == True:
                        student_record = student.return_record()
                        writer.writerow(student_record.split(","))
                    else:
                        print("student hasn't been graded")


        else:
            print("No student has been graded")


        
        
    

        
