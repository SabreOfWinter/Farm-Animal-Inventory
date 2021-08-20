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

        self.frames["All_Details"] = DetailsFrame(container, 'all details')
        self.frames["All_Medical"] = MedicalFrame(container, 'all med')
        self.frames["All_Accounts"] = AccountFrame(container, 'all acco')

        self.frames["Sheep_Details"] = DetailsFrame(container, 'sheep details')
        self.frames["Sheep_Medical"] = MedicalFrame(container, 'sheep med')
        self.frames["Sheep_Accounts"] = AccountFrame(container, 'sheep acco')

        self.frames["Pigs_Details"] = DetailsFrame(container, 'pig details')
        self.frames["Pigs_Medical"] = MedicalFrame(container, 'pig med')
        self.frames["Pigs_Accounts"] = AccountFrame(container, 'pig acco')

        self.frames["Goats_Details"] = DetailsFrame(container, 'goat details')
        self.frames["Goats_Medical"] = MedicalFrame(container, 'goat med')
        self.frames["Goats_Accounts"] = AccountFrame(container, 'goat acco')

        self.frames["Poultry_Details"] = DetailsFrame(container, 'bird details')
        self.frames["Poultry_Medical"] = MedicalFrame(container, 'bird med')
        self.frames["Poultry_Accounts"] = AccountFrame(container, 'bird acco')

        self.frames["Dogs/Cats_Details"] = DetailsFrame(container, 'd/c details')
        self.frames["Dogs/Cats_Medical"] = MedicalFrame(container, 'd/c med')
        self.frames["Dogs/Cats_Accounts"] = AccountFrame(container, 'd/c acco')

        self.frames["Alpacas_Details"] = DetailsFrame(container, 'alpacas details')
        self.frames["Alpacas_Medical"] = MedicalFrame(container, 'alpacas med')
        self.frames["Alpacas_Accounts"] = AccountFrame(container, 'alpacas acco')

        self.change_frame(self.selected_animal)

    def change_frame(self,selected_animal):
        frame = self.frames[str(self.selected_animal.get() + '_' + self.selected_type.get())]
        # frame.reset()
        frame.tkraise()