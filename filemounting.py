import tkinter as tk
from tkinter import filedialog
import pathlib
import logging
import sys

# ------------ DEBUG ------------
debug = True # prints out a bunch of debug info if True
error_flag = False # bandaid fix for error reporting


# -------- FILE OPENING ---------
root = tk.Tk() # some credit to tomvodi/dimakin on stack exchange for tkinker script
root.withdraw()
file_path = filedialog.askopenfilename() # prompts user to select file
file_extension = pathlib.Path(file_path).suffix # gets the file extension from file in filepath
acsavefile = open(file_path, mode = "rb") # opens selected file in read binary mode + names it as a variable
