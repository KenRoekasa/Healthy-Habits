import threading
import time
from tkinter import messagebox

running = True

def hydrate(duration):
    time.sleep(duration)
    messagebox.showinfo("Hydrate", "HYDRATE")

while running:
    hydrate(60*60) # every hour now 

