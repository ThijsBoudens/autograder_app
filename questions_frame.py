import tkinter as tk
from tkinter import ttk
from rubric_widget import *

class Questions_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=2, sticky="nsew")


        self.notebook.bind("<<NotebookTabChanged>>", self.set_currently_selected_question)
    
        
        self.score = 0

    def place_rubrics(self):
        self.clear_frame()
        questions = self.container.questions
        for question in questions:
            row_index = 0
            column_index = 0
            
            question_frame = ttk.Frame(self.notebook)
            question_frame.grid()
            
            self.notebook.add(question_frame, text=question)
            
            rubrics = questions[question].rubrics 
            for rubric in rubrics.values():
                rubric_title = rubric.title
                points = rubric.points
                if len(question_frame.grid_slaves(column=column_index)) == 5:
                    column_index += 1
                    row_index = 0
                
                Rubric_widget(rubric.rubric_ID, question, question_frame, self.container, rubric_title, points).grid(row=row_index, column=column_index, pady=10)
                row_index += 1
           
    
    def clear_frame(self):
        for tab_id in self.notebook.tabs():
            frame = self.notebook.nametowidget(tab_id)
            self.notebook.forget(tab_id)
            frame.destroy()

    def set_currently_selected_question(self, event:tk.Event):
        current_question = self.notebook.tab(tk.CURRENT)["text"]
        self.container.current_question = current_question   
   
    def update_view(self, student):
        # student_rubric_state = self.container.student_rubric_state[student.name]
        for tab_id in self.notebook.tabs():
            tab_name = self.notebook.tab(tab_id,"text")
            frame = self.notebook.nametowidget(tab_id)
            for rubric in frame.winfo_children():
                pass_state = student.questions[tab_name].rubrics[rubric.rubric_ID].pass_state
            
                if pass_state == True:
                    rubric.mark_pass()
                elif pass_state == False:
                    rubric.mark_fail()
                elif pass_state is None:
                    rubric.reset()





