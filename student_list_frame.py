import tkinter as tk
from tkinter import ttk, filedialog
from center_text_box import *
from student import *
import os

class Student_list_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # self.rowconfigure(0, weight=1)
        self.listbox = tk.Listbox(self, font=(None, 20))
        self.listbox.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command = self.listbox.yview)

        self.container = container

    def load_students(self):
        folder_path = filedialog.askdirectory(initialdir=os.getcwd())
        if folder_path:
            self.read_exam_files(folder_path)
            self.container.update_views(None)
        else:
            print("Did not select a folder.")

    def read_exam_files(self, folder_path):
        files = os.listdir(folder_path)

        for file in files:
            #create a student object per exam file
            st = Student(file, folder_path+'/'+file)
            
            # add that student to main's list of students ()
            self.container.add_student(st)

            # add the student to list box
            self.listbox.insert("end", st.id) #only show id for anonymous grading

        self.listbox.bind('<<ListboxSelect>>', lambda event: self.container.update_views(event, reset_questions=True))



    def update(self):
        # give green background to graded students
        for i, student_ID in enumerate(self.listbox.get(0, tk.END)):
            student = self.container.students[student_ID]
            if student.graded:
                self.listbox.itemconfig(i, {"bg":"chartreuse1"})
            else:
                self.listbox.itemconfig(i, {"bg":"DarkGoldenRod1"})
