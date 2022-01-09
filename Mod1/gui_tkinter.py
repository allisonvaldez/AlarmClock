"""
This file is in charge of creating the GUI that TKinter will use. I will
import this file into the main.py file to run it. I wanted to keep the
functionalities of the code separate for design purposes. I completed this by
creating a class wrapper for my code to have mobility throughout the program.
"""

from tkinter import *


# this is the class wrapper
class TheTKWindow:

    def __init__(self):
        # we have to instantiate the object for the class to be able to be used.

        # sets root as a class level variable initialized with the function TK
        self.root = Tk()

        # sets the window title
        self.root.title("Alarm Application")

        # sets the shape and/or geometry of the clock
        self.root.geometry("500x500")

        # set a label for the clock to prompt the user
        Label(self.root, text="Alarm Clock:", font=("Helvetica 20 bold"),
              fg="red").pack(pady=10)
        Label(self.root, text="Set Alarm:", font=("Helvetica 20 bold")).pack

        """
        Frame: adds a frame to the window
        """

        frame = Frame(self.root)
        frame.pack()

        # sets the hour variables
        hour = StringVar(self.root)
        hours = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                 '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                 '20', '21', '22', '23', '24')
        hour.set(hours[0])

        hrs = OptionMenu(frame, hour, *hours)
        hrs.pack(side=LEFT)

        minute = StringVar(self.root)
        minutes = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                   '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                   '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                   '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
                   '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                   '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
                   '60')
        minute.set(minutes[0])

        mins = OptionMenu(frame, minute, *minutes)
        mins.pack(side=LEFT)

        second = StringVar(self.root)
        seconds = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                   '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                   '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                   '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
                   '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                   '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
                   '60')
        second.set(seconds[0])

        secs = OptionMenu(frame, second, *seconds)
        secs.pack(side=LEFT)

        Button(self.root, text="Set Alarm", font=("Helvetica 15 bold")).pack(
            pady=20)

    def begin_clock(self):
        """
        This function is in charge of monitoring the GUI interfaces for any
        changes and updates it as necessary.

        :return: the proper GUI interface update
        """

        """
        runs the event loop to monitor for events or changes for the GUI window
        """
        self.root.mainloop()
