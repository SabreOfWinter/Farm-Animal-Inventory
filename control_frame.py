import tkinter as tk
from tkinter import ttk
from database import *

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

class TopBar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create control variables
        self.selected_type = tk.StringVar(value=master.option_menu_list[0])
        self.selected_animal = tk.StringVar(value=master.animal_option_menu_list[0])


        # OptionMenu
        self.animal_options = tk.OptionMenu(
            self, 
            self.selected_animal, 
            *master.animal_option_menu_list, 
            command=master.change_frame
        ).grid(column=0, row=0, padx=5, pady=5)
        
        # OptionMenu
        self.type_options = tk.OptionMenu(
            self, 
            self.selected_type, 
            *master.option_menu_list, 
            command=master.change_frame
        ).grid(column=1, row=0, padx=5, pady=5)

        self.title = tk.Button(self, text='a').grid(row=0, column=3)
        
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

class ControlFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        #Create database if it doesn't currently exist
        create_tables()

        # Create value lists
        self.option_menu_list = ["Details", "Medical", "Accounts"]
        self.animal_option_menu_list = ["All", "Sheep", "Pigs", "Poultry", "Goats", "Dogs/Cats", "Alpacas"]
        self.frames = [
            [AllDetailsFrame, SheepDetailsFrame, PigsDetailsFrame, PoultryDetailsFrame, GoatsDetailsFrame, DogsAndCatsDetailsFrame, AlpacasDetailsFrame],
            [AllMedicalFrame, SheepMedicalFrame, PigsMedicalFrame, PoultryMedicalFrame, GoatsMedicalFrame, DogsAndCatsMedicalFrame, AlpacasMedicalFrame],
            [AllAccountsFrame, SheepAccountsFrame, PigsAccountsFrame, PoultryAccountsFrame, GoatsAccountsFrame, DogsAndCatsAccountsFrame, AlpacasAccountsFrame]
        ]

        self.navigation = TopBar(self)
        self.frame = AllDetailsFrame(self) #Sets the inital frame to display
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

    def change_frame(self, selected):
        self.frame = self.frames[self.option_menu_list.index(self.navigation.selected_type.get())][self.animal_option_menu_list.index(self.navigation.selected_animal.get())](self)