import time
import curses
import os
import math

sizeOfTerminal = [i for i in os.get_terminal_size()]
XSize = sizeOfTerminal[0] - 2
YSize = sizeOfTerminal[1] - 1

def pbar(window):
    character = '۞'
    timeToSleep = 0.0001
    message = "get gamed"
    curses.curs_set(0)

    window.addstr((YSize // 2), (XSize // 2) - (len(message) // 2), message)
    window.addstr((YSize // 2) + 1, (XSize // 2) - (len(message) // 2), message)

    curses.noecho()
    setter = 0
    while setter < (YSize / 2) + 1:
        window.addstr(setter, setter, '╔')
        for x in range(setter + 1, XSize - setter):
            window.addstr(setter, x, '═')
            window.refresh()
            time.sleep(timeToSleep)

        window.addstr(setter,XSize - setter, '╗')
        for y in range(setter + 1, YSize - setter):
            window.addstr(y, XSize - setter, '║')
            window.refresh()
            time.sleep(timeToSleep)

        window.addstr(YSize - setter, XSize - setter, '╝')
        for x in range(XSize - setter - 1, setter, -1):
            window.addstr(YSize - setter, x, '═')
            window.refresh()
            time.sleep(timeToSleep)

        window.addstr(YSize - setter, setter, '╚')
        for y in range(YSize - setter - 1, setter, -1):
            window.addstr(y, setter, '║')
            window.refresh()
            time.sleep(timeToSleep)

        setter += 1

    # c = window.getch()
    # if c == ord('c'):
    #     break

curses.wrapper(pbar)