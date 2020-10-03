import time

from playsound import playsound

running = True


def hydrate(duration):
    time.sleep(duration)
    playsound('sounds/Hydrate.mp3')
    # messagebox.showinfo("Hydrate", "HYDRATE")


while running:
    hydrate(60 * 60)  # every hour now
