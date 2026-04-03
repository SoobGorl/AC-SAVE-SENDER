import tkinter as tk
from tkinter import messagebox

# implement button states so you cant press stuff when yuo shouldnt lol

window = tk.Tk()
window.geometry("200x300")
window.resizable(False, False)
window.title("ACSS")
dir_window_logo = tk.PhotoImage(file="icon.png")
window.iconphoto(True, dir_window_logo)

label_title = tk.Label(window, text="FIRST TIME SETUP")
label_title.pack(padx=0, pady=0)

dir_setup_image = tk.PhotoImage(file="setup_windowlogo.png")
setup_image = tk.Label(window, image=dir_setup_image)
setup_image.pack()


label_step1 = tk.Label(window, text="Step 1:")
label_step1.pack()
button_step1 = tk.Button(window, text="SELECT YOUR SAVE FILE")
button_step1.pack()

label_step2 = tk.Label(window, text="Step 2:")
label_step2.pack()
button_step2 = tk.Button(window, text="SELECT YOUR GAME ROM")
button_step2.pack()

label_step3 = tk.Label(window, text="Step 3:")
label_step3.pack()
button_step3 = tk.Button(window, text="SELECT DOLPHIN.EXE")
button_step3.pack()

label_step4 = tk.Label(window, text="Step 4:")
label_step4.pack()
def cmd_button_connect():
    messagebox.showerror(title="ERROR_01", message="STEPS HAVE NOT BEEN COMPLETED!\n\n"
                                                   "MAKE SURE ALL BOXES HAVE BEEN CHECKED BEFORE CONTINUING.")
button_step4 = tk.Button(window, text="~ CONNECT! ~", command=cmd_button_connect)
button_step4.pack()



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