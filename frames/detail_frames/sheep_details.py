import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from database import *

class SheepDetailsFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.a = tk.Label(self, text='a').grid(row=0, column=0)
        
        self.cols = ('Tag #', 'Reg Name', 'Breed', 'Sex', 'DOB', 'Date in', 'CPH in', 'Date out', 'CPH out', 'Buy Price', 'Sell Price', 'Ram Tag/Name', 'Eew Tag #', 'On Farm?')

        self.table = ttk.Treeview(self, columns=self.cols, show='headings')
        
        # self.result_label = ttk.Label(self, text=str('shee[' + ' ' + 'a'))
        # self.result_label.grid(row=1, columnspan=3)

        for col in self.cols:
            print(col)
            self.table.heading(col, text=col)

        self.table.grid(row=1, column=0, sticky='nsew')
        self.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")