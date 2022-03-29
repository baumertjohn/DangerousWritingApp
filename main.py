# Day 89 of 100 Days of Code
# Clone of The Most Dangerous Writing App
# https://www.squibler.io/dangerous-writing-prompt-app

from tkinter import *
import tkinter.font as tkFont

# GLOBALS
WINDOW_W = 600  # Window Width
WINDOW_H = 300  # Window Height
timer_count = 10

# Starter Text


def user_input(key):
    global timer_count
    print(key.char)
    try:
        window.after_cancel(timer)
    except NameError:
        pass
    timer_count = 10
    typing_timer()


def typing_timer():
    global timer_count, timer
    print(timer_count)
    timer_count -= 1
    timer = window.after(1000, typing_timer)


# Instructions

# Reset app


def reset():
    # Stop timer
    try:
        window.after_cancel(timer)
    except NameError:
        pass
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
    # Reset button
    reset_button.place(anchor=CENTER, relx=0.5, rely=0.5, y=200)
    # Watch for user typing
    typing_box.bind("<Key>", user_input)


# Setup window for application
window = Tk()
# user_text = StringVar()  # This is for tracking the users input
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
