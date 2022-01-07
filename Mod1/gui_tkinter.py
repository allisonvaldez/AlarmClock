"""
This file is in charge of creating the GUI that TKinter will use. I will
import this file into the main.py file to run it. I wanted to keep the
functionalities of the code separate for design purposes. I completed this by
creating a class wrapper for my code to have mobility throughout the program.
"""

from tkinter import *


# this is the class wrapper
class TheTKWindow:

    # we have to instantiate the object for the class to be able to be used.
    def __init__(self):

        # sets root as a class level variable initialized with the function TK
        self.root = Tk()

        # sets the window title
        self.root.title("Alarm Application")

        # sets the shape and/or geometry of the clock
        self.root.geometry("500x500")


