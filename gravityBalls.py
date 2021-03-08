import time
import curses
import os
import math
import random as rndm

sizeOfTerminal = [i for i in os.get_terminal_size()]
XSize = sizeOfTerminal[0] - 2
YSize = sizeOfTerminal[1] - 1

class Firework:
    def __init__(self, timeToSleep, window, YSize, XSize):
        self.amountOfParticles = 6
        self.YSize = YSize
        self.XSize = XSize
        self.window = window
        self.timeToSleep = timeToSleep
        self.XSpeed = rndm.randint(-40, 40)
        self.YSpeed = rndm.randint(10, 25)
        self.gravity = 9.81
        self.XPos = rndm.randint((XSize // 2) - 5, (XSize // 2) + 5)
        self.YPos = YSize - 1
        self.realXPos = self.XPos
        self.realYPos = self.YPos
        self.exploded = False
        self.delete = False
        self.childrenParticlesList = []
        self.explosionForce = 10
    
    def move(self):
        if self.YPos < YSize:
            self.YSpeed -= self.gravity * self.timeToSleep
            self.realXPos += self.XSpeed * self.timeToSleep
            self.realYPos -= self.YSpeed * self.timeToSleep
            self.XPos = int(self.realXPos)
            self.YPos = int(self.realYPos)
            if self.YPos > 0:
                try:
                    self.window.addstr(self.YPos, self.XPos, '0')
                except:
                    self.XSpeed = self.XSpeed * -1
                    
    def particles_move(self):
        for i in self.childrenParticlesList:
            if i.delete:
                self.childrenParticlesList.remove(i)
            else:
                i.move()

def pbar(window):
    character = '۞'
    timeToSleep = 0.033
    curses.curs_set(0)

    fireworksList = []
    curses.noecho()

    while True:
        createBall = rndm.randint(0, 10)
        if createBall == 1:
            fireworksList.append(Firework(timeToSleep, window, YSize, XSize))
        for firework in fireworksList:
            if firework.delete:
                fireworksList.remove(firework)
            elif not firework.exploded:
                firework.move()
            else:
                firework.particles_move()

            window.refresh()
        
        time.sleep(timeToSleep)

        window.clear()
        
curses.wrapper(pbar)
