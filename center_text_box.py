import tkinter as tk
from tkinter import ttk
import io
import tokenize
import keyword




class Center_textbox(ttk.Frame):
    def __init__(self, container, file_path=None):
        super().__init__(container)
        self.text = tk.Text(self, wrap="word")
        self.text.config(
    font=("Consolas", 12), 
    fg="#00D21F", 
    bg="#000000", 
    insertbackground="white")          
        self.text.pack(expand=True, fill="both")
       
       
    def set_text(self, content):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, content)

        # Tokenize file content
        tokens = list(tokenize.generate_tokens(io.StringIO(content).readline,  ))
        
        # highlight keywords
        keywords = [(token.start[0], token.start[1], token.end[1]) for token in tokens if token.string in keyword.kwlist or token.string=="self"]
        for kw in keywords:
            self.text.tag_add("keyword", f"{kw[0]}.{kw[1]}", f"{kw[0]}.{kw[2]}")


        # highlight strings, comments, operators
        for token in tokens:
            if token.type == tokenize.STRING:
                self.text.tag_add("string", f"{token.start[0]}.{token.start[1]}", f"{token.end[0]}.{token.end[1]}")
            if token.type == tokenize.COMMENT:
                self.text.tag_add("comment", f"{token.start[0]}.{token.start[1]}", f"{token.end[0]}.{token.end[1]}")
            if token.type == tokenize.OP:
                self.text.tag_add("operator", f"{token.start[0]}.{token.start[1]}", f"{token.end[0]}.{token.end[1]}")
        
        # configure highlight colors
        self.text.tag_config("keyword", foreground="#1500FF")
        self.text.tag_config("string", foreground="#FFAA00")
        self.text.tag_config("comment", foreground="#6C6C6C")
        self.text.tag_config("operator", foreground="#EEFF00")
