import tkinter as tk
from tkinter import ttk, filedialog
from center_text_box import *
from student import *
import os
import shutil
import subprocess
import importlib
import traceback
import sys
import copy
import math

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

    def fix_student_directory(self, folder_path):
        #this function will pull all the student files from their subdirectories
        #into root directory (folder_path) and delete the subdirectories afterwards.
        for student_dir in os.listdir(folder_path):
            if os.path.isdir(folder_path+'/'+student_dir):
                for student_f in os.listdir(folder_path+'/'+student_dir):
                    # print(answer2)
                    shutil.copy(folder_path+'/'+student_dir + '/' + student_f, folder_path)
                    shutil.rmtree(folder_path+'/'+student_dir)


        #afterwards, we remove spaces and dots from file names to avoid issues
        for student_file in os.listdir(folder_path):
            oldname = folder_path+'/'+student_file
            newname = oldname.replace(' ', '')
            newname = newname[:-3].replace(".", "") + ".py" 
            # print(newname)
            os.rename(oldname, newname)

    def convert_notebooks(self, file_path):
        #this function will convert any .ipynb files to .py files.
        #then it will delete the ipynb files.
        toremove = []
        for file in os.listdir(file_path):
            if '.ipynb' in file:
                fullpath = file_path + '/' + file
                subprocess.run(['cmd', '/c', "jupyter nbconvert --to script "+fullpath])
                py_name = fullpath.replace('.ipynb', '.py')
                if os.path.isfile(py_name):
                    toremove.append(fullpath)

        for file in toremove:
            os.remove(file)

    def read_exam_files(self, folder_path):

        self.fix_student_directory(folder_path)
        self.convert_notebooks(folder_path)

        files = os.listdir(folder_path)

        for file in files:
            #create a student object per exam file
            st = Student(file, folder_path+'/'+file)
            
            # add that student to main's list of students ()
            self.container.add_student(st)

            # add the student to list box
            self.listbox.insert("end", st.id) #only show id for anonymous grading

        self.listbox.bind('<<ListboxSelect>>', lambda event: self.container.update_views(event, reset_questions=True))




        
    #todo
    #ask for questions/inputs/outputs json file
    #do the autograding
    #update students and rubrics
    #check for timeouts (inf loops)

    def autograde(self):

        #tests file
        file = filedialog.askopenfile(mode ='r', filetypes =[('python files', '*.py')], initialdir=os.getcwd())
        module_name = file.name.split('/')[-1][:-3] #module name without .py
        module = importlib.import_module(module_name)

        tests = {
            'fucntion_names' : module.function_names,
            'function_inputs' : module.function_inputs,
            'function_outputs' : module.function_outputs
        }

        

        for student in self.container.students.values():
            student.autograde(tests)







    def update(self):
        # give green background to graded students
        for i, student_ID in enumerate(self.listbox.get(0, tk.END)):
            student = self.container.students[student_ID]
            if student.graded:
                self.listbox.itemconfig(i, {"bg":"chartreuse1"})
            else:
                self.listbox.itemconfig(i, {"bg":"DarkGoldenRod1"})
