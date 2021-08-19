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

        # Set a minsize for the window, and place it in the middle
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
        x_cordinate = int((self.winfo_screenwidth() / 2) - (self.winfo_width() / 2))
        y_cordinate = int((self.winfo_screenheight() / 2) - (self.winfo_height() / 2))
        self.geometry("+{}+{}".format(x_cordinate, y_cordinate))

if __name__ == "__main__":
    app = App()
    app.mainloop()