# Day 89 of 100 Days of Code
# Clone of The Most Dangerous Writing App
# https://www.squibler.io/dangerous-writing-prompt-app

from tkinter import *
import tkinter.font as tkFont

# GLOBALS
WINDOW_W = 600  # Window Width
WINDOW_H = 300  # Window Height

# Starter Text


def user_input(*args):
    pass


def typing_timer():
    pass


# Instructions

# Reset app
def reset():
    # Clear Instructions
    info_line_1.destroy()
    info_line_2.destroy()
    info_line_3.destroy()
    info_line_4.destroy()
    # Resize window
    window.geometry(f'{WINDOW_W}x{WINDOW_H*2}')
    # Create typing box
    typing_box = Text(width=40, height=20)
    typing_box.place(anchor=CENTER, relx=0.5, rely=0.5, y=-25)
    typing_box.focus_set()
    reset_button.place(anchor=CENTER, relx=0.5, rely=0.5, y=200)


# Setup window for application
window = Tk()
user_text = StringVar()
window.title('A Dangerous Writing App')
window.geometry(f'{WINDOW_W}x{WINDOW_H}')
window.resizable(width=False, height=False)

# Custom Fonts
large_font = tkFont.Font(family='Helvetica', size=14)
medium_font = tkFont.Font(family='Helvetica', size=12)
small_font = tkFont.Font(family='Helvetica', size=10)

# App Instructions
info_line_1 = Label(text='A', justify='center', font=large_font)
info_line_1.place(anchor=CENTER, relx=0.5, rely=0.5, y=-45)
info_line_2 = Label(text='Dangerous', justify='center',
                    font=large_font, fg='red')
info_line_2.place(anchor=CENTER, relx=0.5, rely=0.5, y=-15)
info_line_3 = Label(text='Writing App', justify='center', font=large_font)
info_line_3.place(anchor=CENTER, relx=0.5, rely=0.5, y=15)
info_line_4 = Label(text="Don't stop writing, or all progress will be lost.",
                    justify='center', font=small_font)
info_line_4.place(anchor=CENTER, relx=0.5, rely=0.5, y=45)

# Press button to clear and start
reset_button = Button(text='Start/Reset', command=reset)
reset_button.place(anchor=CENTER, relx=0.5, rely=0.5, y=75)

# Watch for text entering

# If no entry
# Start timer
# If entry
# Restart timer
# Else end game

# End game text

window.mainloop()
