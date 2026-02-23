import tkinter as tk
from tkinter import ttk

class Rubrics(ttk.Frame):
    def __init__(self, container, rubric_title, points):
        super().__init__(container,
                        borderwidth=5,
                        relief="groove")
        self.grid_columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1,2), weight=1)
        self.config(width=15, height=10)

        self.rubric_title = rubric_title
        self.points = points

        self.pass_state = None

        #Rubric name 
        title = tk.Label(self, text=rubric_title)
        title.configure(font=("Helvetica", 10, "bold"))
        title.place(relx=0.5, rely=0.5, anchor="center")
        title.grid(row=0, pady=5)
        
        # Buttons
        self.pass_button = tk.Button(self, text="Pass",font=("bold", 10),width=5, command=self.mark_pass, relief="groove")
        self.pass_button.grid(row=2, column=0, pady=5)
        
        self.fail_button = tk.Button(self, text="Fail",font=("bold", 10) ,width=5, command=self.mark_fail, relief="groove")
        self.fail_button.grid(row=2, column=1, pady=5)


    def mark_pass(self):
        self.pass_button.config(bg="chartreuse2")
        self.fail_button.config(bg="SystemButtonFace")
        self.pass_state = True

    def mark_fail(self):
        self.pass_button.config(bg="SystemButtonFace")
        self.fail_button.config(bg="crimson")
        self.pass_state = False


