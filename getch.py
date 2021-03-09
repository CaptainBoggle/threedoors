class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno() 
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt # msforehead amirite

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

try: # windows first because windows game or something
    getch = _GetchWindows()
except ImportError:
    getch = _GetchUnix()