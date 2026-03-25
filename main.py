import tkinter as tk
from tkinter import ttk, filedialog
import copy
from top_left_buttons_frame import *
from student_list_frame import * 
from center_text_box import *
from top_right_button_frame import *
from questions_frame import *
from student_grade_counter import *
from student import *
from question import *
from rubric import *
import json

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.init_visuals()
        self.init_variables()


    def init_visuals(self):
        self.title("autograder")
        self.screen_width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()

        # Center textbox
        self.textbox = Center_textbox(self)
        self.textbox.grid(column=1, row=1, sticky="nsew")

        # score count 
        self.student_grade_counter = Student_grade_counter(self)

        # Left listbox
        self.listbox = Student_list_frame(self)
        self.listbox.grid(column=0, row=1, sticky="nsew")

        #rubrics container
        self.questions_frame = Questions_frame(self)
        self.questions_frame.grid(column=2, row=1, sticky="nsew")

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
        # self.bind('<Escape>', lambda e: self.destroy())
        #this is dangerous lets remove

    def init_variables(self):
        self.students = {}
        self.questions = {}
        self.student_rubric_state = {}
           
    def update_students_questions(self):
        for stu in self.students:
            self.students[stu].set_questions(copy.deepcopy(self.questions_frame.questions))
            self.students[stu].update()

    def add_student(self, st):
        # dictiorany of students based on unique id (ANR student number)
        self.students[st.id] = st

    def get_selected_student(self):
        index = self.listbox.listbox.curselection()
        if len(index)>0:
            student_id = self.listbox.listbox.get(index)
            return self.students[student_id]
        return None

    def update_views(self, event):
        #this is the main update function. Anything that happens (pick a student,
        #change a rubric, etc) -> this function will be called to update everything.
        #Note: this function will not initialize rubrics and questions per student.

        #fetch selected student, we will need it to update the views.
        selected_student = self.get_selected_student()

        # if student selected
        if selected_student:
            selected_student.update() #check grades
            self.listbox.update() #update the listbox
            self.questions_frame.update_view(selected_student) #update questions/rubrics
            self.student_grade_counter.update(selected_student) #update grade
            self.textbox.update(selected_student)    
 

    # Iterates through questions and rubrics to save points per question and failed rubrics 
    # This function also sets the student.been_graded attribute to True
    # It also calculates the score and displays it at the top 
    def set_results(self):
        # check if currently selected student has already been graded
        if self.current_student and self.current_student.been_graded == False:
            max_points = 0
            total_points = 0
        # iterate through questions 
            for question in self.questions:
                points = 0
                failed_rubrics = []
                # iterate through rubrics 
                for rubric in self.questions[question].rubrics:
                    max_points += self.questions[question].rubrics[rubric].points
    
                    if self.current_student.questions[question].rubrics[rubric].pass_state == True:
                        points += self.questions[question].rubrics[rubric].points
                        total_points += self.questions[question].rubrics[rubric].points
                    elif self.current_student.questions[question].rubrics[rubric].pass_state == False:
                        failed_rubrics.append(self.current_student.questions[question].rubrics[rubric].rubric_ID)
                    else:
                        print("Not all rubrics have been graded.")
                        break

                self.current_student.set_points_per_question(question, points)
                self.current_student.set_failed_rubrics(question, failed_rubrics)
                
                self.current_student.pending = False
                self.current_student.been_graded = True
                
                self.student_grade_counter.display_student_grade(total_points, max_points)
            self.current_student.set_grade()
            print(self.current_student.return_record())

        else:
            print("No one selected or already graded")
        print(self.current_student.points_per_question)
    
            
            
         

def on_resize(event):
    pass
#     print(f"Window resized to: {event.width}x{event.height}")

if __name__=="__main__":
    app = App()
    app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}")
    app.bind("<Configure>", on_resize)
    app.mainloop()