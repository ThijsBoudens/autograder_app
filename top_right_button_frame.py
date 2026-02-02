import tkinter as tk
from tkinter import ttk



class Top_right_buttons_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # self.rowconfigure(0, weight=1)
        self.__create_widgets()

    def __create_widgets(self):
        ttk.Button(self, text="Canvas Export", width=40).grid(column=0, row=0, ipadx=20, ipady=10, padx=10)
        ttk.Button(self, text="Osiris Export", width=40).grid(column=1, row=0, ipadx=20, ipady=10, padx=10)


