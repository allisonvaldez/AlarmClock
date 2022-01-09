"""
Created by Allison Valdez
January 6, 2021
Project: Alarm Clock
"""

"""
This file is used to help expose what functions, classes, etc are available 
to other scripts when the module is imported. This python script will run 
EVERY TIME the module is imported and can contain any code you desire. Here  
we're very simply making it easier for other scripts to access the 
process_files function. Note: other scripts and functions are still accessible
"""

from Mod1.gui_tkinter import TheTKWindow
from Mod1.__main__ import *

print(f"the __init__ file is opened")
