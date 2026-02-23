import tkinter as tk
from tkinter import ttk, filedialog
import os 
from top_left_buttons_frame import *
from student_list_frame import * 
from center_text_box import *
from top_right_button_frame import *
from rubrics_container import *
from score_counter import *
from student import *
import json

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("autograder")

        self.students = {}
        self.current_student = None

        self.questions = None

    

        # Center textbox
        self.textbox = Center_textbox(self)
        self.textbox.grid(column=1, row=1, sticky="nsew")

        # score count 
        self.student_grade_counter = Student_grade_counter(self)
        # self.score_count.grid(column=1, row=0, sticky="nsew")

       
        # Left listbox
        self.listbox = Student_list_frame(self)
        self.listbox.grid(column=0, row=1, sticky="nsew")

        #rubrics container
        self.rubrics_container = Rubrics_container(self)
        self.rubrics_container.grid(column=2, row=1, sticky="nsew")

 
        #Configure grid
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure((0,1,2), weight=1)

        # Top left buttons 
        top_left_button_frame = Top_left_buttons_frame(self)
        top_left_button_frame.grid(column=0, row=0)

        # Top right buttons
        top_right_button_frame = Top_right_buttons_frame(self)
        top_right_button_frame.grid(column=2, row=0)

        #exit app with esc        
        self.bind('<Escape>', lambda e: self.destroy())

    
    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.listbox.list_folder_content(folder_path)
            return    
    
    def load_rubrics(self):
        file = filedialog.askopenfile(mode ='r', filetypes =[('json files', '*.json')])
        if file:
            content = json.load(file)
            self.rubrics_container.place_rubrics(content)
            self.questions = self.rubrics_container.questions
            return
        
    def set_current_student(self, student_name):
        if student_name not in self.students:
            self.students[student_name] = Student(student_name)
        self.current_student = self.students[student_name]
    

    # Iterates through questions and rubrics to save points per question and failed rubrics 
    # This function also sets the student.been_graded attribute to True
    # It also calculates the score and displays it at the top 
    def set_results(self):
        # check if currently selected student has already been graded
        if self.current_student and self.current_student.been_graded == False:
            notebook = self.rubrics_container.winfo_children()[0]
            max_points = 0
            total_points = 0
        # iterate through questions 
            for tab_id, frame in zip(notebook.tabs(), notebook.winfo_children()):
                points = 0
                failed_rubrics = []
                # iterate through rubrics 
                for rubric in frame.winfo_children():
                    max_points += rubric.points
                 
                    if rubric.pass_state == None:
                        return "ungraded rubrics"
                    if rubric.pass_state == True:
                        points += rubric.points
                        total_points += rubric.points
                    elif rubric.pass_state == False:
                        failed_rubrics.append(rubric.rubric_title)

                self.current_student.set_points_per_question(notebook.tab(tab_id, "text"), points)
                self.current_student.set_failed_rubrics(notebook.tab(tab_id, "text"), failed_rubrics)
                
                self.current_student.been_graded = True
                
                self.student_grade_counter.display_student_grade(total_points, max_points)
        
            self.current_student.set_score()
        else:
            print("No one selected or aldready graded")
        print(self.current_student.points_per_question)
  



            # for rubric in tab.winfo_children():
            #     print(rubric.pass_state)
    
    # def reset_rubrics(self):
    #     self.rubrics_container
    

            
            
         

def on_resize(event):
    pass
#     print(f"Window resized to: {event.width}x{event.height}")

if __name__=="__main__":
    app = App()
    app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}")
    app.bind("<Configure>", on_resize)
    app.mainloop()