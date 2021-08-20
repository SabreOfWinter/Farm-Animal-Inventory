import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror

class AccountFrame(ttk.Frame):
    def __init__(self, container, animal_type):
        super().__init__(container)
        print(animal_type)
        if(animal_type == "pig acco"):
            self.test_label = ttk.Label(self, text="Test")
            self.test_label.grid(row=3, columnspan=3)    
        
        self.result_label = ttk.Label(self, text=animal_type)
        self.result_label.grid(row=1, columnspan=3)

        # add padding to the frame and show it
        self.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

        def reset(self):
            self.result_label.text = ''
