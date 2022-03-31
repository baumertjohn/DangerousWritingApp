# Day 89 of 100 Days of Code
# Clone of The Most Dangerous Writing App
# https://www.squibler.io/dangerous-writing-prompt-app

from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont

# GLOBALS
WINDOW_W = 600  # Window Width
WINDOW_H = 300  # Window Height
timer, typing_box = 0, 0  # Set timer and typing_box to zero for first run checks


def user_input(key):
    """Starts and resets timer based on user input."""
    global timer_count
    # print(key.char)  # Debugging line
    # Reset timer after keypress detected
    if timer:
        window.after_cancel(timer)
    # Timer start time
    timer_count = 8  # User gets 2 seconds before timer starts
    timer_label.config(text="")
    typing_timer()


def typing_timer():
    """Countdown timer with checks for starting visual countdown text or
    destroying textbox window at the end."""
    global timer_count, timer
    # print(timer_count)  # Debugging line
    timer_count -= 1
    if timer_count < 6:
        timer_label.config(text=f"{timer_count}", font=TIMER_FONT, fg="red")
    # Destroy text box when timer hits zero
    if timer_count < 0:
        destroy_textbox()
    # Only run timer if above zero
    if timer_count > -1:
        timer = window.after(1000, typing_timer)


def destroy_textbox():
    """Destroys textbox and asks user to save text or start over."""
    global user_text
    user_text = typing_box.get("1.0", "end-1c")
    # print(user_text)  # Debugging line
    typing_box.destroy()
    reset_button.destroy()
    # Stop Timer
    window.after_cancel(timer)
    timer_label.config(text="")
    # Re-start button
    end_label_1 = Label(
        text="Your work is GONE...",
        justify="center",
        font=LARGE_FONT,
    )
    end_label_1.place(anchor=CENTER, relx=0.5, rely=0.5, y=-25)
    end_label_2 = Label(
        text="You can save what you had or try again.",
        justify="center",
        font=SMALL_FONT,
    )
    end_label_2.place(anchor=CENTER, relx=0.5, rely=0.5)
    save_button = Button(text="Save", command=save_work)
    save_button.place(anchor=CENTER, relx=0.5, rely=0.5, y=25)
    start_button = Button(text="Restart", command=reset)
    start_button.place(anchor=CENTER, relx=0.5, rely=0.5, y=75)


def save_work():
    """Open dialog to save the users text."""
    f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return
    f.write(user_text)
    f.close()


# Reset app
def reset():
    """Resizes the window from the starting text or clear the window and stop
    the timer."""
    global timer_label, typing_box, reset_button
    # Resize window
    window.geometry(f"{WINDOW_W}x{WINDOW_H*2}")
    # Clear Instructions
    if info_line_1:
        info_line_1.destroy()
        info_line_2.destroy()
        info_line_3.destroy()
        info_line_4.destroy()
    # Stop timer if user presses reset while typing
    if timer:
        window.after_cancel(timer)
        timer_label.config(text="")
    # Create countdown timer
    timer_label = Label(text="", justify="center", font=LARGE_FONT)
    timer_label.place(anchor=CENTER, relx=0.5, rely=0.1)
    # Create typing box
    if typing_box:
        # Check for existing typing_box if user hits reset button multiple times, etc.
        typing_box.destroy()
        reset_button.destroy()
    typing_box = Text(width=40, height=20, wrap=WORD)
    typing_box.place(anchor=CENTER, relx=0.5, rely=0.5, y=-25)
    typing_box.focus_set()
    # Reset button
    reset_button = Button(text="Reset", command=reset)
    reset_button.place(anchor=CENTER, relx=0.5, rely=0.5, y=200)
    # Watch for user typing
    typing_box.bind("<Key>", user_input)


# Setup window for application
window = Tk()
# Custom Fonts
LARGE_FONT = tkFont.Font(family="Helvetica", size=14)
SMALL_FONT = tkFont.Font(family="Helvetica", size=10)
TIMER_FONT = tkFont.Font(family="Helvetica,", weight="bold", size=40)
# Starting window setup
window.title("A Dangerous Writing App")
window.geometry(f"{WINDOW_W}x{WINDOW_H}")
window.resizable(width=False, height=False)

# App Instructions
info_line_1 = Label(text="A", justify="center", font=LARGE_FONT)
info_line_1.place(anchor=CENTER, relx=0.5, rely=0.5, y=-45)
info_line_2 = Label(text="Dangerous", justify="center", font=LARGE_FONT, fg="red")
info_line_2.place(anchor=CENTER, relx=0.5, rely=0.5, y=-15)
info_line_3 = Label(text="Writing App", justify="center", font=LARGE_FONT)
info_line_3.place(anchor=CENTER, relx=0.5, rely=0.5, y=15)
info_line_4 = Label(
    text="Don't stop writing, or all progress will be lost.",
    justify="center",
    font=SMALL_FONT,
)
info_line_4.place(anchor=CENTER, relx=0.5, rely=0.5, y=45)

# Press button to clear and start
start_button = Button(text="Start", command=reset)
start_button.place(anchor=CENTER, relx=0.5, rely=0.5, y=75)

# End game text

window.mainloop()
