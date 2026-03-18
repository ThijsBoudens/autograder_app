import tkinter as tk
class Rubric_button(tk.Button):
    def __init__(self, container, text, rubric_id, command=None, font=("bold", 10), width=5, relief="groove"):
        super().__init__(container, text=text, command=command, font=font, width=width,relief=relief)
        self.container = container
        self.text = text
        self.rubric_id = rubric_id
        self.color = "SystemButtonFace"
        self.isPressed = False


    
    def reset_view(self):
        self.color = "SystemButtonFace"

    
    def change_state(self, color):
        self.color = color 
        self.config(bg=self.color)
        self.isPressed = not self.isPressed
