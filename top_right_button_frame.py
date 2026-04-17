import tkinter as tk
from tkinter import ttk
import csv
import pickle
import datetime
from tkinter import messagebox
from tkinter import ttk, filedialog
import os




class Top_right_buttons_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container 
        ttk.Button(self, text="Save", width=(0.05*self.container.screen_width), command=self.save).grid(column=1, row=0)
        ttk.Button(self, text="Load", width=(0.05*self.container.screen_width), command=self.load).grid(column=2, row=0)

        ttk.Button(self, text="Export csv", width=(0.05*self.container.screen_width), command=self.export_csv).grid(column=3, row=0)

        for widget in self.winfo_children():
            widget.grid(ipadx=10, ipady=10, padx=10)

    def save(self):
        if len(self.container.students)>0 and len(self.container.questions)>0:
            print('Saving...')
            big_dict = {
                'students': self.container.students,
                'exams_dir': self.container.listbox.students_dir,
                'rubrics_dir': self.container.questions_frame.rubrics_dir
            }
            # print(big_dict)
            fname = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')+ '.pickle'
            with open('save_'+fname, 'wb') as pkl:
                pickle.dump(big_dict, pkl, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            messagebox.showerror("Error", "Please load exams and/or rubrics first.")
        print('Done saving.')

    def load(self):
        print('Loading...')
        file = filedialog.askopenfile(mode ='r', filetypes =[('pickle files', '*.pickle')], initialdir=os.getcwd())
        with open(file.name, 'rb') as pkl:
            big_dict = pickle.load(pkl)

        self.container.listbox.load_students(big_dict['exams_dir'])
        self.container.questions_frame.load_rubrics(big_dict['rubrics_dir'])
        self.container.students = big_dict['students']
        self.container.update_views(None)
        print('Done loading.')

    def export_csv(self):
        firstLine = 'Last name,First name,ANR,'
        for q in self.container.questions.values():
            firstLine += f'{q.id},Rubrics,'
        firstLine+='Total'

        with open("results.csv", "w", encoding='utf-8') as csvfile:
            csvfile.write(firstLine+'\n')
            for student in self.container.students.values():
                # print(student.name)
                student_record = student.get_record()
                csvfile.write(student_record+'\n')



        
        
    

        
