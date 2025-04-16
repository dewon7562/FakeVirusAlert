#!/usr/bin/env python3

# fake_virus_alert.py
# Trolling tool to display a fake virus alert with a countdown timer

import tkinter as tk
from tkinter import messagebox
import time
import random

def update_timer():
    global seconds_left
    if seconds_left > 0:
        seconds_left -= 1
        timer_label.config(text=f"Time until files are DELETED: {seconds_left} seconds")
        root.after(1000, update_timer)
    else:
        messagebox.showerror("VIRUS ALERT", "All your files have been DELETED! Just kidding, but you're trolled!")
        root.destroy()

# Create main window
root = tk.Tk()
root.title("VIRUS DETECTED")
root.geometry("400x200")
root.resizable(False, False)

# Fake virus message
message = tk.Label(root, text="WARNING: VIRUS DETECTED!\nYour system is infected with TrollVirus!", fg="red", font=("Arial", 14))
message.pack(pady=20)

# Countdown timer
seconds_left = random.randint(30, 120)  # Random countdown between 30 and 120 seconds
timer_label = tk.Label(root, text=f"Time until files are DELETED: {seconds_left} seconds", font=("Arial", 12))
timer_label.pack(pady=20)

# Start timer
root.after(1000, update_timer)

# Run the application
root.mainloop()
