import tkinter as tk
from tkinter import ttk
from rubric_button import *

class Rubric_widget(ttk.Frame):
    def __init__(self, rubric_ID, question_ID, container, controller, rubric_title, points):
        super().__init__(container,
                        borderwidth=5,
                        relief="groove")
        self.grid_columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1,2), weight=1)
        self.config(width=15, height=10)
        self.controller = controller

        self.rubric_title = rubric_title
        self.points = points

        self.question_ID = question_ID
        self.rubric_ID = rubric_ID
        self.pass_state = None

        #Rubric name 
        title = tk.Label(self, text=rubric_title)
        title.configure(font=("Helvetica", 10, "bold"))
        title.place(relx=0.5, rely=0.5, anchor="center")
        title.grid(row=0, pady=5)
        
        # Buttons
        self.pass_button = Rubric_button(self, "Pass", self.rubric_ID, command=self.mark_pass)
        self.pass_button.grid(row=2, column=0, pady=5)
        
        self.fail_button = Rubric_button(self, "Fail", self.rubric_ID, command=self.mark_fail)
        self.fail_button.grid(row=2, column=1, pady=5)


    #update=True. Set to False to avoid infinite loop (update views that update this that update views etc.)    
    def mark_pass(self, update=True):
        self.pass_button.config(bg="chartreuse2")
        self.fail_button.config(bg="SystemButtonFace")
        self.pass_state = True
        self.controller.get_selected_student().questions[self.question_ID].rubrics[self.rubric_ID].passed = self.pass_state
        if update:
            self.controller.update_views(None)

    def mark_fail(self, update=True):
        self.pass_button.config(bg="SystemButtonFace")
        self.fail_button.config(bg="crimson")
        self.pass_state = False
        self.controller.get_selected_student().questions[self.question_ID].rubrics[self.rubric_ID].passed = self.pass_state
        if update:
            self.controller.update_views(None)
    
    def reset(self):
        self.pass_button.config(bg="SystemButtonFace")
        self.fail_button.config(bg="SystemButtonFace")
        self.pass_state = None



    
