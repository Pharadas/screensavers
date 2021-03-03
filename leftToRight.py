import time
import curses
import os
import math
import random

sizeOfTerminal = [i for i in os.get_terminal_size()]
XSize = sizeOfTerminal[0] - 2
YSize = sizeOfTerminal[1] - 1

def pbar(window):
    character = '۞'
    timeToSleep = 0.0001
    message = "gaming"
    curses.curs_set(0)

    window.addstr((YSize // 2), (XSize // 2) - (len(message) // 2), message)
    window.addstr((YSize // 2) + 1, (XSize // 2) - (len(message) // 2), message)

    while True:
        while True:
            curses.echo()
            height = 0
            character = '▓'
            while height < YSize:
                if height % 2 == 0:
                # window.addstr(height, setter, '╔')
                    for x in range(XSize):
                        window.addstr(height, x, character) # random.random_choice(['1, 0'])
                        window.refresh()
                        time.sleep(timeToSleep)
                else:
                    for x in range(XSize, 0, -1):
                        window.addstr(height, x, character)
                        window.refresh()
                        time.sleep(timeToSleep)

                height += 1

            character = '█'
            while height > 0:
                if height % 2 == 0:
                # window.addstr(height, setter, '╔')
                    for x in range(XSize):
                        window.addstr(height, x, character) # random.random_choice(['1, 0'])
                        window.refresh()
                        time.sleep(timeToSleep)
                else:
                    for x in range(XSize, 0, -1):
                        window.addstr(height, x, character)
                        window.refresh()
                        time.sleep(timeToSleep)

                height -= 1

        c = window.getch()
        if c == ord('c'):
            break

curses.wrapper(pbar)