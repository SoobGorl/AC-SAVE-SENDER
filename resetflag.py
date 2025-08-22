from trust_evaluation import *

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
for address in reset_address:
    if debug:
        print(reset_flag(reset_address[address])) # prints out the current value from the above addresses in number form
    else:
        pass
    if reset_flag(reset_address[address]) == 0:
        reset_active = False
    elif error_flag:
        logging.warning("UNSPECIFIED ERROR. MOST LIKELY, RESET ADDRESS WAS NOT FOUND.")
        break # if error tripped, stop and break here
    else:
        reset_active = True

# ------- RESET REPORTING --------
if reset_active:
    print("A save is actively opened, or the reset flag has been tripped. RESET_ACTIVE STATE:" + str(reset_active))
elif error_flag: # find out how to specify this lol, some universal error thing. same goes for the rest of these!!!
    logging.critical("AN ERROR UNSPECIFIED ERROR OCCURRED. SAVE STATE COULD NOT BE DETERMINED.")
    sys.exit()
else:
    print("The save is currently inactive/closed. RESET_ACTIVE STATE: " + str(reset_active))