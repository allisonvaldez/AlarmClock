"""
Created by Allison Valdez
January 6, 2021
Project: Alarm Clock

See the README for important project notes and intentions for the project.
"""

# Import Required Library
from tkinter import *
from playsound import playsound
import datetime
import time
from threading import *

"""
Root is set at the global level of the program.
1. A root object will be created with the TK() method to make the window
2. We set the object's display window to 600X600
"""
root = Tk()
root.geometry("600x600")

def Threading():
	"""
	Threading is the process of having multiple processes execute at the same
	time to simultaneous execution. Insert more notes later

	:return:  the proper alarm determined by the user
	"""
	t1=Thread(target=alarm)
	t1.start()

def alarm():
	"""
	This function is in charge of setting the alarm for our program. The
	while loop sets the code to automatically trigger the program to run
	when opened.

	:return: alarm
	"""
	while True:
		# this gathers the input from the user on the alarm time selected
		set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"

		# the program should lag by 1 second before executing further code
		time.sleep(1)

		# this allows us to get the current time and formats it to hms string
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time,set_alarm)

		# simple statement to check if the current time is the alarm time
		if current_time == set_alarm:
			print("Time to Wake up")
			# This is incharge of playing the alarm when the time is reached
			playsound('audio.mp3')

# Add Labels, Frame, Button, Optionmenus
Label(root,text="Simple Alarm Clock Application",font=("Helvetica 20 bold"),
	  fg="red").pack(pady=10)
Label(root,text="Set Your Alarm:",font=("Helvetica 15 bold")).pack()

# insert notes about the frame
frame = Frame(root)
frame.pack()

# constructs a string variable to hold the number of hours
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)

# this automatically sets the display of hours to the index at 0 (00)
hour.set(hours[0])

# this displays the number of hours to the left based on our input
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

# constructs a string variable to hold the number of minutes
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')

# this automatically sets the display of minutes to the index at 0 (00)
minute.set(minutes[0])

# this displays the number of minutes to the left based on our input
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

# constructs a string variable to hold the number of seconds
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')

# this automatically sets the display of seconds to the index at 0 (00)
second.set(seconds[0])

# this displays the number of seconds to the left based on our input
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,text="Set Your Alarm",font=("Helvetica 15"),command=Threading).pack(
	pady=20)

"""
This runs an event loop that listens for events from the user. It makes sure 
the block code written after this line until the user closes the windown (or 
finishes their tasks."""
root.mainloop()




