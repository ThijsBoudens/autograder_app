import tkinter as tk
from tkinter import ttk
from center_text_box import *
from student import *
import os

class Student_list_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # self.rowconfigure(0, weight=1)
        self.listbox = tk.Listbox(self, font=(None, 20), )
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
        self.listbox.bind('<<ListboxSelect>>', lambda e: (self.get_file_content(folder_path), self.get_student_name(), self.highlight_student(), self.update_questions_frame()))



    def get_file_content(self, folder):
        selected_indice = self.listbox.curselection()
        file_name = self.listbox.get(selected_indice)
        selected_file_path = folder+"/"+file_name
        with open(selected_file_path, 'r') as f:
            content = f.read()
            self.container.textbox.set_text(content)
        
    
    def get_student_name(self):
        selected_indice = self.listbox.curselection()
        name = self.listbox.get(selected_indice)[:-3]
        self.container.set_current_student(name)

    def highlight_student(self):
        for i, student_name in enumerate(self.listbox.get(0, tk.END)):
            student_name = student_name[:-3]
            if student_name in self.container.students:
                student = self.container.students[student_name]
                if student.been_graded == True:
                    self.listbox.itemconfig(i, {"bg":"chartreuse1"})
                
                elif student.been_graded == False and student.pending == True:
                    self.listbox.itemconfig(i, {"bg":"DarkGoldenRod1"})

                else:
                    pass
   
    def update_questions_frame(self):
        self.container.update_questions_frame()         

