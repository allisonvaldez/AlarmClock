"""
Created by Allison Valdez
January 6, 2021
Project: Alarm Clock

See the README for important project notes and intentions for the project.
"""

from Mod1.gui_main_window import MainWindow

print(f"the __main__ file is opened")

"""
This calls the TKWindow class and utilizes the functions declared to run the 
GUI window.
"""
clock_window = MainWindow()
clock_window.start_clock()
