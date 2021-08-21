import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror

from frames.detail_frames.all_details import AllDetailsFrame
from frames.medical_frames.all_medical import AllMedicalFrame
from frames.accounts_frames.all_accounts import AllAccountsFrame

from frames.detail_frames.sheep_details import SheepDetailsFrame
from frames.medical_frames.sheep_medical import SheepMedicalFrame
from frames.accounts_frames.sheep_accounts import SheepAccountsFrame

from frames.detail_frames.pigs_details import PigsDetailsFrame
from frames.medical_frames.pigs_medical import PigsMedicalFrame
from frames.accounts_frames.pigs_accounts import PigsAccountsFrame

from frames.detail_frames.poultry_details import PoultryDetailsFrame
from frames.medical_frames.poultry_medical import PoultryMedicalFrame
from frames.accounts_frames.poultry_accounts import PoultryAccountsFrame

from frames.detail_frames.goats_details import GoatsDetailsFrame
from frames.medical_frames.goats_medical import GoatsMedicalFrame
from frames.accounts_frames.goats_accounts import GoatsAccountsFrame

from frames.detail_frames.dogs_and_cats_details import DogsAndCatsDetailsFrame
from frames.medical_frames.dogs_and_cats_medical import DogsAndCatsMedicalFrame
from frames.accounts_frames.dogs_and_cats_accounts import DogsAndCatsAccountsFrame

from frames.detail_frames.alpacas_details import AlpacasDetailsFrame
from frames.medical_frames.alpacas_medical import AlpacasMedicalFrame
from frames.accounts_frames.alpacas_accounts import AlpacasAccountsFrame

from database import *

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

        self.frames["All_Details"] = AllDetailsFrame(container)
        self.frames["All_Medical"] = AllMedicalFrame(container)
        self.frames["All_Accounts"] = AllAccountsFrame(container)

        self.frames["Sheep_Details"] = SheepDetailsFrame(container)
        self.frames["Sheep_Medical"] = SheepMedicalFrame(container)
        self.frames["Sheep_Accounts"] = SheepAccountsFrame(container)

        self.frames["Pigs_Details"] = PigsDetailsFrame(container)
        self.frames["Pigs_Medical"] = PigsMedicalFrame(container)
        self.frames["Pigs_Accounts"] = PigsAccountsFrame(container)

        self.frames["Poultry_Details"] = PoultryDetailsFrame(container)
        self.frames["Poultry_Medical"] = PoultryMedicalFrame(container)
        self.frames["Poultry_Accounts"] = PoultryAccountsFrame(container)

        self.frames["Goats_Details"] = GoatsDetailsFrame(container)
        self.frames["Goats_Medical"] = GoatsMedicalFrame(container)
        self.frames["Goats_Accounts"] = GoatsAccountsFrame(container)

        self.frames["Dogs/Cats_Details"] = DogsAndCatsDetailsFrame(container)
        self.frames["Dogs/Cats_Medical"] = DogsAndCatsMedicalFrame(container)
        self.frames["Dogs/Cats_Accounts"] = DogsAndCatsAccountsFrame(container)

        self.frames["Alpacas_Details"] = AlpacasDetailsFrame(container)
        self.frames["Alpacas_Medical"] = AlpacasMedicalFrame(container)
        self.frames["Alpacas_Accounts"] = AlpacasAccountsFrame(container)

        self.change_frame(self.selected_animal)

    def change_frame(self,selected_animal):
        frame = self.frames[str(self.selected_animal.get() + '_' + self.selected_type.get())]
        frame.reset()
        frame.tkraise()