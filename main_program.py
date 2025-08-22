from trust_evaluation import *

if file_trust == 4:
    from resetflag import *
elif file_trust == -1:
    # from resetflag import *
    logging.critical("VALID GCI FILE, BUT HEADERS DO NOT EXIST! ACDX OR GAMESHARK SAVE? TERMINATING FOR SAFETY.")
    sys.exit()
else:
    logging.critical("FILE DID NOT PASS THE NECESSARY CHECKS FOR VALIDATION.")
    sys.exit()

# main program would run at this point. if validation is bad, then it's stopped, and if it's good, reset check is run, and you get that value
# stuff could be improved with functions but I really will only be calling the reset flag, but that's future stuff
print("Main program is ready to go! :)")