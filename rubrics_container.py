import tkinter as tk
from tkinter import ttk
from rubrics import *

class Rubrics_container(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=2, sticky="nsew")
        self.questions = []
    
        
        self.score = 0

    def place_rubrics(self, file_content):
        self.clear_frame()

        questions = file_content['rubrics']
        for question in questions:
            self.questions.append(question)
            row_index = 0
            column_index = 0
            
            question_frame = ttk.Frame(self.notebook)
            question_frame.grid()
            
            self.notebook.add(question_frame, text=question)
            for rubric in questions[question]:
                rubric_title = questions[question][rubric]["title"]
                points = questions[question][rubric]["points"]
                if len(question_frame.grid_slaves(column=column_index)) == 5:
                    column_index += 1
                    row_index = 0
                
                Rubrics(question_frame, rubric_title, points).grid(row=row_index, column=column_index, pady=10)
                row_index += 1
           
    
    def clear_frame(self):
        for tab_id in self.notebook.tabs():
            frame = self.notebook.nametowidget(tab_id)
            self.notebook.forget(tab_id)
            frame.destroy()

    
   






    #     self.__create_widget()
    
    # def __create_widget(self):
    #     frame = ttk.Frame(self)
    #     frame.columnconfigure(0, weight=1)
    #     frame.rowconfigure(0, weight=1)
    #     frame.rowconfigure((1,2,3,4,5), weight=10)
    #     frame.pack(ipadx=10, ipady=1, expand=False)
        
    #     rubric_1 = Rubrics(frame, "rubrics 1", "is even")
    #     rubric_1.focus()
    #     rubric_1.grid(row=1, column=0)

    #     rubric_2 = Rubrics(frame, "rubrics 2", "return integer")
    #     rubric_2.focus()
    #     rubric_2.grid(row=4, column=0)
        


