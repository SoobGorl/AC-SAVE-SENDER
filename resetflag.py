import tkinter as tk
from tkinter import filedialog
import logging
import pathlib
import sys

# TODO! check if file has animal crossing header

# ------------ DEBUG ------------
debug = True # prints out a bunch of debug info if True
error_flag = False # bandaid fix for error reporting

# ------- TRUST REPORTING -------
file_trust = 0 # value changes through checks to ensure that the selected file is an ACGC one
save_likelyhood = { # defines what the file_trust number means for humans
    0: "NOT A VALID FILE",
    1: "VALID .GCI FILE",
    2: "VALID RESET ADDRESSES",
    3: "VALID GAME HEADER", # not yet implemented
    4: "UNKNOWN FILE, SEMI-VALID"
}
def trust_reporter(): # prints out trust number, then the trust message/state
    print("SAVE LIKELYHOOD: " + str(file_trust) + ", " + save_likelyhood[file_trust])

# -------- FILE OPENING ---------
#root = tk.Tk() # creates file-specific open dialog through tkinter
#root.withdraw() # (credit to tomvodi/dimakin on stack exchange for this script)
#file_path = filedialog.askopenfilename() # prompts user to select file
#file_extension = pathlib.Path(file_path).suffix # gets the file extension from file in filepath
#acsavefile = open(file_path, mode = "rb") # opens selected file in read binary mode + names it as a variable
acsavefile = open("RESETFLAG.gci", mode = "rb")



def bytes_to_string(address, byte_length):
    acsavefile.seek(address)
    return acsavefile.read(byte_length).decode('UTF-8')



print(bytes_to_string(0x0, 25))

#if str(acsavefile.read(25)) == "b'GAFE01\xff\x01DobutsunomoriP_MU'":
#    print("check good")
#else:
#    print("check bad")

acsavefile.seek(0x40)
actext_check = acsavefile.read(15)

acsavefile.seek(0x60)
acsavefile.read(8)


#print(header_check)
#if actext_check == "GAFE01\xff\x01DobutsunomoriP_MU":
#    print("header has passed check")
#else:
#    "header not passed"
#print(actext_check)
#if actext_check == "Animal Crossing":
#    print("animal crossing subheader passed")
#else:
#    "subheader not passed"

sys.exit()
# look for "ANIMAL CROSSING" text
# look for town name
# look for villagers
# separate file validity checks from flag checking
# check flags ONLY after validity

# security will be a larger issue but these are basic checks to see if the file is mostly an AC file
"""check after file is recieved if safe
parse entire file and make sure its correct and cant execute bad stuff
when you recieve a file (clientside) verify that file is safe
if all verifications succeed and is valid data/save file, then use it"""

# -------- GCI HANDLING ---------
valid_gci = False # sets initial value to False, as it hasn't been checked yet
if file_extension == ".gci": # if the selected file has the extension .gci, then continue code
    valid_gci = True
    file_trust = 1 # sets trust value to one. originally added the value, but this is more fool-proof, though the program is linear
else:
    file_trust = 0 # for safety :)
    logging.critical("SELECTED FILE DID NOT CONTAIN .GCI EXTENSION")
    pass

# ------------ DEBUG ------------ # may be redundant...
if debug: # reports if file is a .GCI
    print("Chosen file = " + file_path)
    # print("Is .GCI? = " + str(valid_gci))
    trust_reporter()
else:
    pass

# --- DEFINE RESET ADDRESSES ---
reset_address = {
    1: 0x00027156, # the 4 addresses the game checks to see if a player is in the reset state.
    2: 0x00027157, # these addresses do not count the NUMBER of times the player has reset.
    3: 0x0004D156, # if the value at these addresses is 0 (0x0), then a reset is not flagged.
    4: 0x0004D157
}

# ------------ DEBUG ------------
if debug: # prints all addresses
    for address in reset_address.values():
        print(hex(address))
else:
    pass

# ------ READ ADDRESS VALUE ------
def reset_flag(reset_byte): # function reads the given address in its argument, and converts the value inside into a number
    try:
        acsavefile.seek(reset_byte) # the address is inserted here to search
        return acsavefile.read(1)[0] # use hex() to convert this to hexcode. [0] here displays it as a number/hex value.
    except (IndexError, SyntaxError, NameError) as terminal_error: # TODO! SyntaxError and NameError don't work. Why? :c is this redundant? maybe.
        global error_flag # allows these variables to be edited
        error_flag = True
        global file_trust
        file_trust = 0
        return "THERE WAS AN ERROR READING THE GIVEN BYTE (" + str(hex(reset_byte)) + ")", terminal_error

# -------- RESET HANDLING --------
reset_active = False # boolean that checks if a save is active (using the game's reset/resetti flag)
# the below goes through each key in the reset_address dictionary and passes it through the argument of reset_flag
# to convert them into usable numbers.

if not error_flag: # if the error flag isn't tripped, then set file trust to 2
    file_trust = 2
elif error_flag:
    logging.critical("You're not supposed to be here.")
    sys.exit()

for address in reset_address:
    if debug:
        print(reset_flag(reset_address[address])) # prints out the current value from the above addresses in number form
    else:
        pass
    if reset_flag(reset_address[address]) == 0:
        reset_active = False
    elif error_flag:
        logging.critical("UNSPECIFIED ERROR. MOST LIKELY, RESET ADDRESS WAS NOT FOUND.")
        break # if error tripped, stop and break here
    else:
        reset_active = True

# ------------ DEBUG ------------
if debug:
    trust_reporter() # print current trust state
else:
    pass

# ------- RESET REPORTING --------
if reset_active:
    print("A save is actively opened, or the reset flag has been tripped. RESET_ACTIVE STATE:" + str(reset_active))
elif error_flag: # find out how to specify this lol, some universal error thing. same goes for the rest of these!!!
    logging.critical("AN ERROR UNSPECIFIED ERROR OCCURRED. SAVE STATE COULD NOT BE DETERMINED.")
    sys.exit()
else:
    print("The save is currently inactive/closed. RESET_ACTIVE STATE: " + str(reset_active))

# ------ EDGECASE ERROR, NOT GCI BUT SUCCEEDED ALL OTHER CHECKS ------
if not valid_gci and file_trust == 2:
    logging.warning("INVALID .GCI EXTENSION. GAME SHARK SAVE? SUCCESSFULLY RAN ALL OTHER TESTS.")
else:
    pass # REMOVE THIS ENTIRE THING WHEN THE ACTUAL CHECK WORKS,