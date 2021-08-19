import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror

class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)
