# Day 89 of 100 Days of Code
# Clone of The Most Dangerous Writing App
# https://www.squibler.io/dangerous-writing-prompt-app

from tkinter import *
import tkinter.font as tkFont

# GLOBALS
WINDOW_W = 600  # Window Width
WINDOW_H = 300  # Window Height
timer = 0

# Starter Text


def user_input(key):
    global timer_count
    print(key.char)
    if timer:
        window.after_cancel(timer)
    # Timer start time
    timer_count = 8
    timer_label.config(text='')
    typing_timer()


def typing_timer():
    global timer_count, timer
    print(timer_count)
    timer_count -= 1
    if timer_count < 6:
        timer_label.config(text=f'{timer_count}', font=TIMER_FONT, fg='red')
    if timer_count < 0:
        destroy_textbox()
    if timer_count > -1:
        timer = window.after(1000, typing_timer)


def destroy_textbox():
    user_text = typing_box.get('1.0', 'end-1c')
    print(user_text)
    reset_button.invoke()

# Instructions


# Reset app
def reset():
    global timer_label, typing_box
    # Stop timer
    if timer:
        window.after_cancel(timer)
        timer_label.config(text='')
    # Clear Instructions
    info_line_1.destroy()
    info_line_2.destroy()
    info_line_3.destroy()
    info_line_4.destroy()
    # Resize window
    window.geometry(f'{WINDOW_W}x{WINDOW_H*2}')
    # Countdown timer
    timer_label = Label(text='', justify='center', font=LARGE_FONT)
    timer_label.place(anchor=CENTER, relx=0.5, rely=0.1)
    # Create typing box
    typing_box = Text(width=40, height=20, wrap=WORD)
    typing_box.place(anchor=CENTER, relx=0.5, rely=0.5, y=-25)
    typing_box.focus_set()
    # Reset button
    reset_button.place(anchor=CENTER, relx=0.5, rely=0.5, y=200)
    # Watch for user typing
    typing_box.bind("<Key>", user_input)


# Setup window for application
window = Tk()
# Custom Fonts
LARGE_FONT = tkFont.Font(family='Helvetica', size=14)
SMALL_FONT = tkFont.Font(family='Helvetica', size=10)
TIMER_FONT = tkFont.Font(family='Helvetica,', weight='bold', size=40)
# Starting window setup
window.title('A Dangerous Writing App')
window.geometry(f'{WINDOW_W}x{WINDOW_H}')
window.resizable(width=False, height=False)


# App Instructions
info_line_1 = Label(text='A', justify='center', font=LARGE_FONT)
info_line_1.place(anchor=CENTER, relx=0.5, rely=0.5, y=-45)
info_line_2 = Label(text='Dangerous', justify='center',
                    font=LARGE_FONT, fg='red')
info_line_2.place(anchor=CENTER, relx=0.5, rely=0.5, y=-15)
info_line_3 = Label(text='Writing App', justify='center', font=LARGE_FONT)
info_line_3.place(anchor=CENTER, relx=0.5, rely=0.5, y=15)
info_line_4 = Label(text="Don't stop writing, or all progress will be lost.",
                    justify='center', font=SMALL_FONT)
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
