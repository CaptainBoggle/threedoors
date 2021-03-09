

import doors

def process(ch):
    if ch in [1,2,3]:
        doors.opendoor(ch)
    else:
        print("That is not a door!")
        process(ch)

    
