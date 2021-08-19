import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Farm Animal Inventory')
        self.resizable(False, False)

        # Simply set the theme
        self.tk.call("source", "sun-valley.tcl")
        self.tk.call("set_theme", "dark")

if __name__ == "__main__":
    app = App()
    app.mainloop()