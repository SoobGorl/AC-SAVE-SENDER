import pathlib
import sys
import builtins
from datetime import datetime

file_path = "RESETFLAG.gci" # change this whenever opening a save
debug = False

# override print statement show it shows the time and also saves each line to a file (very inefficient, sue me)
def print(*args, log_file='log_validation.txt', **kwargs):
    timestamp = datetime.now().strftime("%m-%d-%y / %I:%M:%S %p |")
    message = " ".join(map(str, args))
    full_output = f"{timestamp} {message}"
    builtins.print(full_output, **kwargs)
    with open(log_file, 'a') as file:
        file.write(full_output + '\n')

def bytes_to_string(address, byte_length): # turns things to strings so I can parse them easier
    acsavefile.seek(address)
    return acsavefile.read(byte_length)

reset_address = [0x00027156, 0x00027157, 0x0004D156, 0x0004D157]

def reset_flag(reset_byte): # function reads the given address in its argument, and converts the value inside into a number
    try:
        acsavefile.seek(reset_byte) # the address is inserted here to search
        return acsavefile.read(1)[0] # use hex() to convert this to hexcode. [0] here displays it as a number/hex value.
    except (IndexError, SyntaxError, NameError) as terminal_error: # this is sort of redundant, since it checks for the bytes? NO IT DOESNT?????
        file_trust = 0
        print("[IO CRITICAL] COULD NOT LOCATE BYTE (OUT OF RANGE?)")

def file_management(x):

    if x == "open":
        print("[INFO] RUNNING VALIDATION CHECKS...")
        global acsavefile
        global file_extension
        acsavefile = open(file_path, mode="rb")
        file_extension = pathlib.Path(file_path).suffix  # gets the file extension from file in filepath
        print(f"[IO] OPENING FILE: {file_path}")

    if x == "close":
        acsavefile.close()
        print(f"[IO] CLOSING FILE: {file_path}")

    if x == "validate": # oh my god this is so messy, fix this eventually

        global file_trust
        file_trust = 0

        if debug == True:
            print("[DEBUG] FILE GAMEID HEADER: " + str(bytes_to_string(0x0, 15)))
            print("[DEBUG] FILE SUBHEADER: " + str(bytes_to_string(0x40, 15)))
            print("[DEBUG] FILE TOWN NAME: " + str(bytes_to_string(0x60, 8)))

        # check extension
        if file_extension == ".gci":  # if the selected file has the extension .gci, then continue code
            file_trust = 1  # sets trust value to one. originally added the value, but this is more fool-proof, though the program is linear
        else:
            file_trust = 0  # for safety :) (i dont need this, i just think id lose track of this value very easily, lol? peace of mind)
            print("[IO WARNING] SELECTED FILE DID NOT CONTAIN .GCI EXTENSION")

        # check game header
        if bytes_to_string(0x0, 25) == b'GAFE01\xff\x01DobutsunomoriP_MU':
            file_trust = 2
        else:
            file_trust = 0
            print("[IO WARNING] GAMEID HEADER DOES NOT MATCH")

        # check subheader
        if bytes_to_string(0x40, 15) == b'Animal Crossing':
            file_trust = 3
        else:
            file_trust = 0
            print("[IO WARNING] SUBHEADER DOES NOT MATCH")

        # OOPS, YOU NEED TO VALIDATE THAT THE RESET BYTES EVEN EXIST! YOU DONT NEED TO, BUT SHOULD! this is done for "for address in reset address"

        # if even 1 check fails, throw validation error
        if file_trust == 3:
            pass
        else:
            print("[IO CRITICAL] FILE NOT VALID")
            # sys.exit()

    if x == "state":
        for address in reset_address:
            if reset_flag(address) == 0:  #
                reset_active = False
            else:
                reset_active = True # should it return these values?
        if reset_active:
            print("[IO INFO] SAVE IS OPEN")
        else:
            print("[IO INFO] SAVE IS CLOSED")

# WRITE IF IT PASSED CHECKS FOR VALIDATION

def whole_shebang(filepath):
    file_management("open")
    file_management("validate")
    # file_management("state")
    file_management("close")
