"""
Created by Allison Valdez
January 6, 2021
Project: Alarm Clock
"""


"""
This file is in charge of creating the GUI that TKinter will use. I will
import this file into the __main__.py file to run it. I wanted to keep the
functionalities of the code separate for design purposes. I completed this by
creating a class wrapper for my code to have mobility throughout the program.
"""

from tkinter import *
from Mod1.left_panel import *
from Mod1.right_panel import *
import datetime
import time
from beepy import beep

print(f"the gui_tkinter file is opened")


# this is the class wrapper
class MainWindow:

    def __init__(self):
        # we have to instantiate the object for the class to be able to be used.

        # sets root as a class level variable initialized with the function TK
        self.root = Tk()

        # sets the window title
        self.root.title("Alarm Application")

        # sets the shape and/or geometry of the clock
        self.root.geometry("500x500")

        # sets the background color of the window
        self.root.config(background = "#FFFFFF")

        # sets a frame for the left and right handside
        self.left_frame = Frame(self.root, width=200, height=600)
        self.left_frame.grid(row=0, column=0, padx=10, pady=2)
        self.right_frame = Frame(self.root, width=200, height=300)
        self.right_frame.grid(row=0, column=1, padx=10, pady=2)

        """"""
        """sets the hour variable to a string and makes it to automatically 
        populate with 00 when it is displayed."""
        """
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
            pady=20)"""

    def start_clock(self):
        """
        This function is in charge of monitoring the GUI interfaces for any
        changes and updates it as necessary.

        :return: the proper GUI interface update
        """
        print(f"begin clock function triggered")
        """
        runs the event loop to monitor for events or changes for the GUI window
        """
        self.root.mainloop()

    """def sound_alarm(timer):
        """
    """This function takes the parameter (argument) of timer in order to play
    the alarm. It only contains a while loop of a boolean function (
    automatically set to true) which makes this function automatically set to
    triggered to be set to work.

    :param timer: The alarm time that triggers the alarm
    :return: An alarm being played"""
    """

    print(f"beginning alarm function triggered")

    while True:
        print(f"while true statement triggered")
        """
    """ .sleep(1) halts the execution of further commands by 1 second until we 
     receive the time or prompt from the user. """
    """
    time.sleep(1)

    """
    """get the current time (date and time) and save it to the current_time 
    variable to use later """
    """
    current_time = datetime.datetime.now()

    # string conversion to format the time to display as H:M:S
    current_time_now = current_time.strftime("%H:%M%S")

    # string conversion to format the date to display as d/m/y
    current_date_now = current_time.strftime("%d/%m/%Y")

    print(f"The date set is:", current_date_now)
    print(f"The current time is", current_time_now)

    """
    """Set an if statement to check if the timer is the same time as the 
    current time recorded. If they are equal then the alarm should sound. 
    Tried to utilize winsound but it will not import for me to call the 
    functions to sound the alarm--but I chose to use beepy instead."""
    """
    if current_time_now == timer:
        print(f"if current time = alarm if statement triggered")
        print(f"The alarm sounded. It is:", current_time_now)
        beep(sound="ping")
        break


def actual_time(hours, mins, secs):
"""


""" This function takes in the user input (in the proper string format) for the
 alarm time they wish to trigger. This takes the same parameter arguement
 as the function above.

 :param hours: parameter of hour gathered from the user
 :param mins: parameter of min gathered from the user
 :param secs: parameter of second gathered from the user
 :return: the proper time format gathered from the user"""
"""
print(f"actual time function triggered")

# Gets the time inputed from the user
timer = f"{hours.__get__()}:{mins.__get__()}:{secs.__get__()}"

hours.__get__()

"""
""" triggers the alarm function above based on the input gathered from the 
 user"""
"""
sound_alarm(timer)

"""
