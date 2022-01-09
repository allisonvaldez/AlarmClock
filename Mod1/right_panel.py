"""
Created by Allison Valdez
January 6, 2021
Project: Alarm Clock

This file is in charge of creating the left panel that will hold the items of
the application. For instance the instructions and other buttons necessary. I
followed the tutorials from here:
https://hackr.io/blog/python-projects
https://robotic-controls.com/learn/python-guis/python-gui-broken-multiple-files
https://data-flair.training/blogs/alarm-clock-python/
https://www.geeksforgeeks.org/creat-an-alarm-clock-using-tkinter/
"""


from tkinter import *


class RightPanel:
    def __init__(self, root, frame):
        """
        Initialize the left panel with all the elements that it requires to run.

        :param root: creates the element window
        :param frame: creates the frame for the window
        """
        self.root = root
        self.frame = frame

