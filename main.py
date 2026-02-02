import tkinter as tk
from tkinter import ttk, filedialog
import os 
from top_left_buttons_frame import *
from student_list_frame import * 
from center_text_box import *
from top_right_button_frame import *
from rubrics_container import *
    
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("autograder")
        self.attributes("-fullscreen", True)
        self.textbox = Center_textbox(self)
        self.textbox.grid(column=1, row=1, sticky="nsew")

 
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

        # list of students
        student_list_frame = Student_list_frame(self)
        student_list_frame.grid(column=0, row=1, sticky="nsew")

        #rubrics container
        rubrics_box = Rubrics_box(self)
        rubrics_box.grid(column=2, row=1, sticky="nsew")
                
        self.bind('<Escape>', lambda e: self.destroy())
    
    def load_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        if os.path.basename(file_path)[-3:] != ".py":
            self.textbox.set_text("Wrong file type")
            return
        
        with open(file_path, "r") as f:
            content = f.read()
            self.textbox.set_text(content)
            return



if __name__=="__main__":
    app = App()
    app.mainloop()