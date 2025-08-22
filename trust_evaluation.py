from filemounting import *

# security will be a larger issue but these are basic checks to see if the file is mostly an AC file"

# ------- TRUST REPORTING -------
file_trust = 0 # value changes through checks to ensure that the selected file is an ACGC one
save_likelyhood = { # defines what the file_trust number means for humans
    0: "NOT A VALID FILE",
    1: "VALID .GCI FILE",
    2: "VALID RESET ADDRESSES", # this is unused but could be useful
    3: "VALID GAME HEADER",
    4: "VALID AC SUBHEADER",
    -1: "UNKNOWN FILE, SEMI-VALID"
}
def trust_reporter(): # prints out trust number, then the trust message/state
    print("SAVE LIKELYHOOD: " + str(file_trust) + ", " + save_likelyhood[file_trust])

# turns address and the number of bytes given into text
def bytes_to_string(address, byte_length):
    acsavefile.seek(address)
    return acsavefile.read(byte_length)

# ------------ DEBUG ------------
if debug: # prints information about file
    print("FILE'S GAMEID HEADER: " + str(bytes_to_string(0x0, 15)))
    print("FILE'S 'AC' SUBHEADER: " + str(bytes_to_string(0x40, 15)))
    print("FILE'S TOWN NAME: " + str(bytes_to_string(0x60, 8))) # not used for trust check, just nice info to have

# -------- GCI HANDLING ---------
if file_extension == ".gci": # if the selected file has the extension .gci, then continue code
    file_trust = 1 # sets trust value to one. originally added the value, but this is more fool-proof, though the program is linear
else:
    file_trust = 0 # for safety :)
    logging.critical("SELECTED FILE DID NOT CONTAIN .GCI EXTENSION")

# ------ HEADER HANDLING -------
if bytes_to_string(0x0, 25) == b'GAFE01\xff\x01DobutsunomoriP_MU': # checks if the bytes at this location match with the default bytes
    file_trust = 3
else:
    file_trust = 0
    if debug:
        logging.warning("GAMEID HEADER DOES NOT MATCH!")

if bytes_to_string(0x40, 15) == b'Animal Crossing': # same as the above trust check, just at a different location
    file_trust = 4
else:
    file_trust = 0
    if debug:
        logging.warning("AC SUBHEADER DOES NOT MATCH!")

# ------------ DEBUG ------------
if debug:
    trust_reporter()  # print current trust state