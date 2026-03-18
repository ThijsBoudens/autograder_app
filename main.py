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
        self.title("autograder")
        self.screen_width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()

        self.students = {}
        self.current_student = None

        self.questions = {}
        self.current_question = None

        self.student_rubric_state = {}


        self.max_points = None

    

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
            for qi, q in enumerate(content["rubrics"]):
                question = Question(qi)
                self.questions[q] = question
                for ri, rubric in enumerate(content["rubrics"][q]):
                    rubric_ID = f"{qi}.{ri}"
                    question.rubrics[rubric_ID] = Rubric(rubric_ID,
                                                           content["rubrics"][q][rubric]["title"], 
                                                            content["rubrics"][q][rubric]["points"])
                question.total_points = sum([rubric.points for rubric in question.rubrics.values()])
            self.max_points = sum([question.total_points for question in self.questions.values()])      
            
            self.questions_frame.place_rubrics()
            return
    
    def get_student(self, student_id):
        if student_id in self.students:
            return self.students[student_id]
        else:
            print("student not found")
        
    
    
    def set_current_student(self, student_name):
        if student_name not in self.students:
            self.students[student_name] = Student(student_name)
        
        self.current_student = self.students[student_name]

        if self.questions and not self.current_student.questions:
            self.current_student.questions = copy.deepcopy(self.questions)
        return

        # if self.questions and student_name not in self.student_rubric_state:
        #     self.student_rubric_state[student_name] = {r_ID:None for q in self.questions.values() for r_ID in q.rubrics}
        
       
    
 

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
    

    def update_questions_frame(self):
        self.questions_frame.update_view(self.current_student)


            # for rubric in tab.winfo_children():
            #     print(rubric.pass_state)
    
    # def reset_rubrics(self):
    #     self.questions_frame
    

            
            
         

def on_resize(event):
    pass
#     print(f"Window resized to: {event.width}x{event.height}")

if __name__=="__main__":
    app = App()
    app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}")
    app.bind("<Configure>", on_resize)
    app.mainloop()