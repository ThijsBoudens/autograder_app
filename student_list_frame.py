import tkinter as tk
from tkinter import ttk, filedialog
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

    def load_students(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.read_exam_files(folder_path)
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

        self.listbox.bind('<<ListboxSelect>>', self.container.update_views)

    def update(self):
        # print('updating student list frame!')
        pass

    


        
    
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
