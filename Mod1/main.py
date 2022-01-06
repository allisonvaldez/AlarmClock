"""
Created by Allison Valdez
January 6, 2021
Project: Alarm Clock
See the README for important project notes and intentions for the project.
"""

"""
1. Tkinter: creates a dialog box to provide: information or to method to gather 
it from the user, a fast & easy way to create GUI applications, 
and a powerful object orientated interface to the TK GUI toolkit.
2. datetime: combines the date and time information gathered from the module (
mostly for dates)
3. time: usually used for Unix systems timestamps (mostly for timing)
4. winsound: enables sound playing mechanism in window systems
"""


from tkinter import *
import datetime
import time
import winsound


def sound_alarm(timer):
    """
    This function takes the parameter (argument) of timer in order to play
    the alarm. It only contains a while loop of a boolean function (
    automatically set to true) which makes this function automatically set to
    triggered to be set to work.

    :param timer: The alarm time that triggers the alarm
    :return: An alarm being played
    """

    while True:
        """
        .sleep(1) halts the execution of further commands until we receive 
        a time value from the user. 
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

def actual_time():
    """

    :return:
    """








