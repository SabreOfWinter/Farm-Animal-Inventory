import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror

class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)

        # Create value lists
        self.option_menu_list = ["", "Details", "Medical", "Accounts"]
        self.animal_option_menu_list = ["", "All" "Sheep", "Pigs", "Geese"]

        # Create control variables
        self.selected_type = tk.StringVar(value=self.option_menu_list[1])
        self.selected_animal = tk.StringVar(value=self.animal_option_menu_list[1])