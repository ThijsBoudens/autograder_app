import tkinter as tk
from tkinter import ttk, filedialog
from rubric_widget import *
import json
import copy
from question import *
from rubric import *

class Questions_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.notebook = ttk.Notebook(self)
        self.questions = {}
        self.notebook.grid(row=1, column=2, sticky="nsew")

        self.notebook.bind("<<NotebookTabChanged>>", self.set_currently_selected_question)
    
        
        self.score = 0

    def load_rubrics(self):
        file = filedialog.askopenfile(mode ='r', filetypes =[('json files', '*.json')])
        if file:
            content = json.load(file)
            for qi, q in enumerate(content["rubrics"]):
                question = Question(q)
                self.questions[q] = question
                for ri, rubric in enumerate(content["rubrics"][q]):
                    rubric_title = content["rubrics"][q][rubric]["title"]
                    rubric_points = content["rubrics"][q][rubric]["points"]
                    rubric = Rubric(ri, rubric_title, rubric_points)
                    question.add_rubric(rubric)
                self.container.questions[q] = question


            self.container.update_students_questions()
            self.place_rubrics()
            self.container.update_views(None)
        else:
            print('No file was selected')

    def place_rubrics(self):
        self.clear_frame()
        for question in self.questions:
            question_id = self.questions[question].id
            row_index = 0
            column_index = 0
            
            question_frame = ttk.Frame(self.notebook)
            question_frame.grid()
            
            self.notebook.add(question_frame, text=question_id)
            
            rubrics = self.questions[question].rubrics 
            for rubric in rubrics.values():
                rubric_title = rubric.title
                points = rubric.points
                if len(question_frame.grid_slaves(column=column_index)) == 5:
                    column_index += 1
                    row_index = 0
                
                Rubric_widget(rubric.id, question_id, question_frame, self.container, rubric_title, points).grid(row=row_index, column=column_index, pady=10)
                row_index += 1
           
    
    def clear_frame(self):
        for tab_id in self.notebook.tabs():
            frame = self.notebook.nametowidget(tab_id)
            self.notebook.forget(tab_id)
            frame.destroy()

    def set_currently_selected_question(self, event:tk.Event):
        current_question = self.notebook.tab(tk.CURRENT)["text"]
        self.container.current_question = current_question   
   
    def update(self, student):
        # student_rubric_state = self.container.student_rubric_state[student.name]
        for tab_id in self.notebook.tabs():
            tab_name = self.notebook.tab(tab_id,"text")
            frame = self.notebook.nametowidget(tab_id)
            for rubric in frame.winfo_children():
                pass_state = student.questions[tab_name].rubrics[rubric.rubric_ID].passed
            
                if pass_state == True:
                    rubric.mark_pass(False)
                elif pass_state == False:
                    rubric.mark_fail(False)
                elif pass_state is None:
                    rubric.reset()





