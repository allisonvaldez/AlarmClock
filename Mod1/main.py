"""
Created by Allison Valdez
January 6, 2021
Project: Alarm Clock

See the README for important project notes and intentions for the project.
"""

import datetime
import time
import winsound
from Mod1.gui_tkinter import TheTKWindow


def sound_alarm(timer):
    """
    This function takes the parameter (argument) of timer in order to play
    the alarm. It only contains a while loop of a boolean function (
    automatically set to true) which makes this function automatically set to
    triggered to be set to work.

    :param winsound:
    :param timer: The alarm time that triggers the alarm
    :return: An alarm being played
    """

    while True:
        """
        .sleep(1) halts the execution of further commands by 1 second until we 
        receive the time or prompt from the user. 
        """
        time.sleep(1)

        """
        get the current time (date and time) and save it to the current_time 
        variable to use later 
        """
        current_time = datetime.datetime.now()

        # string conversion to format the time to display as H:M:S
        current_time_now = current_time.strftime("%H:%M%S")

        # string conversion to format the date to display as d/m/y
        current_date_now = current_time.strftime("%d/%m/%Y")

        print(f"The date set is:", current_date_now)
        print(f"The current time is", current_time_now)

        """
        Set an if statement to check if the timer is the same time as the 
        current time recorded. If they are equal then the alarm should sound.
        
        winsound.PlaySound(sound, flag): returns an immediate asynchronous 
        sound based on two arguments (sound title and flag). It will display a 
        message that the sound is being played.
        """
        if current_time_now == timer:
            print(f"The alarm sounded. It is:", current_time_now)
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break


def actual_time(hours, mins, secs):
    """
    This function takes in the user input (in the proper string format) for the
    alarm time they wish to trigger. This takes the same parameter arguement
    as the function above.

    :param hours: parameter of hour gathered from the user
    :param mins: parameter of min gathered from the user
    :param secs: parameter of second gathered from the user
    :return: the proper time format gathered from the user
    """

    # Gets the time inputed from the user
    timer = f"{hours.__get__()}:{mins.__get__()}:{secs.__get__()}"

    hours.__get__()

    """
    triggers the alarm function above based on the input gathered from the 
    user
    """
    sound_alarm(timer)


"""
This calls the TKWindow class and utilizes the functions declared to run the 
GUI window.
"""
clock_window = TheTKWindow()
clock_window.begin_clock()
