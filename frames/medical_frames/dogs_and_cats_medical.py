import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from database import *

class DogsAndCatsMedicalFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.b = tk.Label(self, text='b').grid(row=0, column=0)

        self.cols = ('ID', 'Name')

        self.table = ttk.Treeview(self, columns=self.cols, show='headings')
        
        # self.result_label = ttk.Label(self, text=str('shee[' + ' ' + 'a'))
        # self.result_label.grid(row=1, columnspan=3)

        for col in self.cols:
            print(col)
            self.table.heading(col, text=col)

        self.table.grid(row=1, column=0, sticky='nsew')

        self.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")