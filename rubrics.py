import tkinter as tk
from tkinter import ttk

class Rubrics(ttk.Frame):
    def __init__(self, container, rubric_name, condition):
        super().__init__(container,
                        borderwidth=5,
                        relief="groove",
                        width=200)
        self.grid_columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2), weight=1)

        #Rubric name 
        title = tk.Label(self, text=rubric_name)
        title.configure(font=("Helvetica", 10, "bold"))
        title.place(relx=0.5, rely=0.5, anchor="center")
        title.grid(row=0, column=1, pady=10)
        
        # Rubric condition
        condition = tk.Label(self, text=condition)
        condition.configure(font=(None, 10))
        condition.grid(row=1, pady=15)
        condition.place(relx=0.5, rely=0.5, anchor="center")
        
       
        # Buttons
        ttk.Button(self, text="Pass", width=20).grid(row=2, column=0, pady=10)
        ttk.Button(self, text="Fail", width=20).grid(row=2, column=2, pady=10)
    


        