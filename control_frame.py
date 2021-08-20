import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror
from details_frame import DetailsFrame
from medical_frame import MedicalFrame
from account_frame import AccountFrame

class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)

        # Create value lists
        self.option_menu_list = ["", "Details", "Medical", "Accounts"]
        self.animal_option_menu_list = ["", "All", "Sheep", "Pigs", "Poultry", "Goats", "Dogs/Cats", "Alpacas"]

        # Create control variables
        self.selected_type = tk.StringVar(value=self.option_menu_list[1])
        self.selected_animal = tk.StringVar(value=self.animal_option_menu_list[1])

        # OptionMenu
        ttk.OptionMenu(
            self, 
            self.selected_animal, 
            *self.animal_option_menu_list, 
            command=self.change_frame
        ).grid(column=0, row=0, padx=5, pady=5)
        
        # OptionMenu
        ttk.OptionMenu(
            self, 
            self.selected_type, 
            *self.option_menu_list, 
            command=self.change_frame
        ).grid(column=1, row=0, padx=5, pady=5)

        self.grid(column=0, row=0, padx=5, pady=5, sticky='ew')

        # initialize frames
        self.frames = {}
        
        for animal_index in range(1, len(self.animal_option_menu_list)):
            animal = self.animal_option_menu_list[animal_index]  

            self.frames[str(animal + "_Details")] = DetailsFrame(container, str(animal + ' details'))
            self.frames[str(animal + "_Medical")] = DetailsFrame(container, str(animal + ' medical'))
            self.frames[str(animal + "_Accounts")] = DetailsFrame(container, str(animal + ' accounts'))

        self.change_frame(self.selected_animal)

    def change_frame(self,selected_animal):
        frame = self.frames[str(self.selected_animal.get() + '_' + self.selected_type.get())]
        # frame.reset()
        frame.tkraise()