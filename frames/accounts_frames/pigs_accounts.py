import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from database import *

class PigsAccountsFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)      

    def reset(self):
        pass