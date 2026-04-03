import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pathlib

window = tk.Tk()
window.geometry("300x200")
window.resizable(False, False)

window.title("LOADIN' STUFF") # maybe have stuff load in the background so it doesnt load all of python before this, doing it here (so you know it launches, since python takes ages to launch first time)
dir_window_logo = tk.PhotoImage(file="icon.png")
window.iconphoto(True, dir_window_logo)

dir_setup_image = tk.PhotoImage(file="loading_windowimage.png")
setup_image = tk.Label(window, image=dir_setup_image)
setup_image.pack()

# check the config file, check if the locations match up and everything (rom, save, emulator) (print stuff to console--if all good then continue)

# if error, then:
# messagebox.showerror(title="ERROR_05", message="YOUR CONFIG FILE IS CORRUPTED OR HAS BEEN CHANGED IN A WAY I DONT UNDERSTAND! PLEASE REDO SETUP")
# and when you press "ok" it deletes the config file and sends you back to the first time setup window

window.mainloop()