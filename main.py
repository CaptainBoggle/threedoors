
import getch
import procinput
import doors



if __name__ == '__main__':
    while(True):
        procinput.process(getch.getch().lower())
        doors.generatedoors() # Say something like "At the back of the room, you notice three doors," describe doors

# Show three doors 
# Await door choice

# Above function will call the battle function, supplying data of chosen door

# Battle function will call loot function

Door 2 is an interesting one... It is 