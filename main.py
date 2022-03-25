# Day 89 of 100 Days of Code
# Clone of The Most Dangerous Writing App
# https://www.squibler.io/dangerous-writing-prompt-app

from tkinter import *
import tkinter.font as tkFont

# GLOBALS

# Starter Text


def user_input(*args):
    pass


def typing_timer():
    pass


# Instructions

# Reset app


# Setup window for application
window = Tk()
user_text = StringVar()
window.title('A Dangerous Writing App')
window.geometry('600x600')
window.resizable(width=False, height=False)

# Custom Fonts
large_font = tkFont.Font(family='Helvetica', size=14)
medium_font = tkFont.Font(family='Helvetica', size=12)
small_font = tkFont.Font(family='Helvetica', size=10)

# Game Instructions
# Press button to clear and start

# Make text input box

# Watch for text entering

# If no entry
# Start timer
# If entry
# Restart timer
# Else end game

# End game text

window.mainloop()
