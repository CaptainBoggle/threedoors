
import getch
import procinput
import doors



if __name__ == '__main__':
    while(True):
        doors.generatedoors()
        procinput.process(getch.getch().lower())
        