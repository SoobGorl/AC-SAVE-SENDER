acsavefile = open("RESETFLAG.gci", mode = "rb") # .gci file to be read
# TODO! check if file exists and if it does check if it's in .gci format

# the 4 addresses the game checks to see if a player is in the reset state.
# these addresses do not count the NUMBER of times the player has reset.
# if the value at these addresses is 0 (0x0), then a reset is not flagged.
reset_address = {
    1: 0x00027156,
    2: 0x00027157,
    3: 0x0004D156,
    4: 0x0004D157
}

# prints all addresses, redundant but gives me a visual
for address in reset_address.values():
    print(hex(address))

# function reads the given address in its argument, and converts it to a value
def reset_flag(reset_byte):
    try:
        acsavefile.seek(reset_byte) # the address is inserted here to search
        return acsavefile.read(1)[0] # use hex() to convert this to hexcode. [0] here displays it as a number/hex value.
    except (IndexError, SyntaxError, NameError) as terminal_error: # TODO! SyntaxError and NameError don't work. Why? :c
        return "THERE WAS AN ERROR READING THE GIVEN BYTE (" + str(hex(reset_byte)) + ")", terminal_error

# goes through each key in the reset_address dictionary and passes it through the argument of reset_flag to convert them into usable numbers.
for address in reset_address:
    print(reset_flag(reset_address[address]))

# older version for reference when i inevitably forget how this works lol
#print(reset_flag(reset_address[1]))
#print(reset_flag(reset_address[2]))
#print(reset_flag(reset_address[3]))
#print(reset_flag(reset_address[4]))