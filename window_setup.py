import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pathlib

# implement button states so you cant press stuff when yuo shouldnt lol
# implement the checkboxes being checked when you open a file/do the thing
# implement the ACTUAL checks (for validity) so you dont open a .mp3 as your save lol

# write the paths and extensions in a text file somewhere so when the window launches

# for unspecified error (exception, etc) itll just be error_00

# WINDOW CONFIG

window = tk.Tk()
window.geometry("200x300")
window.resizable(False, False)

window.title("SASE") # sable able save enabler lol, credits to salvage
dir_window_logo = tk.PhotoImage(file="icon.png")
window.iconphoto(True, dir_window_logo)


# FIRST TIME SETUP

label_title = tk.Label(window, text="FIRST TIME SETUP")
label_title.pack(padx=0, pady=0)

dir_setup_image = tk.PhotoImage(file="setup_windowlogo.png")
setup_image = tk.Label(window, image=dir_setup_image)
setup_image.pack()

# STEP ONE

label_step1 = tk.Label(window, text="Step 1:")
label_step1.pack()

def cmd_open_save():
    file_path = filedialog.askopenfilename()  # prompts user to select file
    file_extension = pathlib.Path(file_path).suffix  # gets the file extension from file in filepath
    # acsavefile = open(file_path, mode="rb")  # opens selected file in read binary mode + names it as a variable
    print(file_path)
    print(file_extension)
    # do the checking part after this
    # ERROR_01 if save is not right format or some check is bad with it (allow continue in future for servers who dnc about the file being sent)

step1_frame = tk.Frame(window)
step1_frame.columnconfigure(0, weight=1)

button_step1 = tk.Button(step1_frame, text="SELECT YOUR SAVE FILE", command=cmd_open_save)
button_step1.grid(row=0, column=1)

checkbox_step1 = tk.Checkbutton(step1_frame)
checkbox_step1.grid(row=0, column=0)

step1_frame.pack()

# STEP TWO

label_step2 = tk.Label(window, text="Step 2:")
label_step2.pack()

def cmd_open_rom():
    file_path = filedialog.askopenfilename()  # prompts user to select file
    file_extension = pathlib.Path(file_path).suffix  # gets the file extension from file in filepath
    print(file_path)
    print(file_extension)
    # ERROR_02 if the rom is in an odd format (.exe), only accept .rvz and .iso (and the other one). Can skip this one, and continue

step2_frame = tk.Frame(window)
step2_frame.columnconfigure(0, weight=1)

button_step2 = tk.Button(step2_frame, text="SELECT YOUR GAME ROM", command=cmd_open_rom)
button_step2.grid(row=0, column=1)

checkbox_step2 = tk.Checkbutton(step2_frame)
checkbox_step2.grid(row=0, column=0)

step2_frame.pack()

# STEP 3

label_step3 = tk.Label(window, text="Step 3:")
label_step3.pack()

def cmd_open_dolphin():
    file_path = filedialog.askopenfilename()  # prompts user to select file
    file_extension = pathlib.Path(file_path).suffix  # gets the file extension from file in filepath
    print(file_path)
    print(file_extension)
    # ERROR_03 file is not an exe or has word "dolphin" in it (see if dolphin has file headers?)

step3_frame = tk.Frame(window)
step3_frame.columnconfigure(0, weight=1)

button_step3 = tk.Button(step3_frame, text="SELECT YOUR GAME ROM", command=cmd_open_dolphin)
button_step3.grid(row=0, column=1)

checkbox_step3 = tk.Checkbutton(step3_frame)
checkbox_step3.grid(row=0, column=0)

step3_frame.pack()

# STEP 4

label_step4 = tk.Label(window, text="Step 4:")
label_step4.pack()

def cmd_button_connect():
    messagebox.showerror(title="ERROR_04", message="STEPS HAVE NOT BEEN COMPLETED!\n\n"
                                                   "MAKE SURE ALL BOXES HAVE BEEN CHECKED BEFORE CONTINUING.")


button_step4 = tk.Button(window, text="     CONNECT!     ", command=cmd_button_connect)
button_step4.pack()

# CLOSING AND RUN

def on_closing():
    if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?\n\n"
                                                  "Make sure your game has been saved, and your save synced!\n"
                                                  "(currently not checked by the application)"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()












"""import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("200x300")
window.title("ACSS")

label = tk.Label(window, text="hi")
label.pack(padx=20, pady=20)

entry = tk.Entry(window) # no multiline
entry.pack()

textbox = tk.Text(window, height=3, width=15)
textbox.pack()

check_state = tk.IntVar()
check = tk.Checkbutton(window, text="press me", variable=check_state)
check.pack()

def show_message():
    print('hi')
    print(check_state.get())
    if check_state.get() == 0:
        print(textbox.get('1.0', tk.END))
    else:
        messagebox.showinfo(title="message", message=textbox.get('1.0', tk.END))


button = tk.Button(window, text="show message", command=show_message)
button.pack()

window.mainloop()"""













"""import tkinter as tk

window = tk.Tk()

window.geometry("200x300")
window.title("ACSS")

label = tk.Label(window, text="hi")
label.pack(padx=20, pady=20)

textbox = tk.Text(window, height=3, width=15)
textbox.pack()

entry = tk.Entry(window) # no multiline
entry.pack()

button = tk.Button(window, text="hi")
button.pack()

frame = tk.Frame(window)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
button1 = tk.Button(frame, text="1")
button1.grid(row=0, column=0)
button2 = tk.Button(frame, text="2")
button2.grid(row=1, column=0)
button3 = tk.Button(frame, text="3")
button3.grid(row=2, column=1)
frame.pack()

buttonsize = tk.Button(window, text="custom width")
buttonsize.place(x=20, y=40, height=100, width=100)

window.mainloop()
"""









"""import tkinter as tk

window = tk.Tk()
window.geometry("200x300")
window.title("ACSS")

label = tk.Label(window, text="hi")
label.pack(padx=20, pady=20)

entry = tk.Entry(window) # no multiline
entry.pack()

check_state = tk.IntVar()
check = tk.Checkbutton(window, text="press me", variable=check_state)
check.pack()

def show_message():
    print('hi')

button = tk.Button(window, text="show message", command=show_message)
button.pack()

window.mainloop()"""