import time
import curses
import os
import math
import random as rndm

sizeOfTerminal = [i for i in os.get_terminal_size()]
XSize = sizeOfTerminal[0] - 2
YSize = sizeOfTerminal[1] - 1

class FireworkParticles:
    def __init__(self, timeToSleep, window, YSize, XSize, XPos, YPos, YSpeed, XSpeed):
        self.YSize = YSize
        self.XSize = XSize
        self.window = window
        self.timeToSleep = timeToSleep
        self.XSpeed = XSpeed
        self.YSpeed = YSpeed
        self.gravity = 9.81
        self.XPos = XPos
        self.YPos = YPos
        self.realXPos = self.XPos
        self.realYPos = self.YPos
        self.delete = False

    def move(self):
        if self.YPos < YSize:
            self.YSpeed -= self.gravity * self.timeToSleep
            self.realXPos += self.XSpeed * self.timeToSleep
            self.realYPos -= self.YSpeed * self.timeToSleep
            self.XPos = int(self.realXPos)
            self.YPos = int(self.realYPos)
            if self.YPos > 0:
                try:
                    self.window.addstr(self.YPos, self.XPos, '.')
                except:
                    self.XSpeed = self.XSpeed * -1
            else:
                self.delete = True

class Firework:
    def __init__(self, timeToSleep, window, YSize, XSize):
        self.amountOfParticles = 5
        self.YSize = YSize
        self.XSize = XSize
        self.window = window
        self.timeToSleep = timeToSleep
        self.XSpeed = rndm.randint(-40, 40)
        self.YSpeed = rndm.randint(10, 35)
        self.gravity = 9.81
        self.XPos = rndm.randint((XSize // 2) - 5, (XSize // 2) + 5)
        self.YPos = YSize - 1
        self.realXPos = self.XPos
        self.realYPos = self.YPos
        self.exploded = False
        self.delete = False
        self.childrenParticlesList = []
        self.explosionForce = rndm.randint(5, 15)
    
    def move(self):
        if self.YSpeed > -5:
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
                else:
                    self.delete = True

        else:
            self.exploded = True
            for r in range(-1, 2, 2):
                movelength = self.explosionForce / self.amountOfParticles
                XSpeed = self.explosionForce / 2
                for i in range(self.amountOfParticles + 1):
                    rest = ((self.explosionForce / 2) ** 2) - (round(XSpeed) ** 2)
                    try:
                        if rest != 0:
                            YSpeed = math.sqrt(rest)  
                        elif self.explosionForce // XSpeed > 0:
                            YSpeed = round(self.explosionForce / XSpeed)
                        else:
                            YSpeed = round(self.explosionForce / XSpeed) * -1
                    except:
                        YSpeed = 0
                    self.childrenParticlesList.append(FireworkParticles(self.timeToSleep, self.window, self.YSize, self.XSize, self.XPos, self.YPos, YSpeed * r, XSpeed))
                    XSpeed -= movelength
                
            self.childrenParticlesList.append(FireworkParticles(self.timeToSleep, self.window, self.YSize, self.XSize, self.XPos, self.YPos, 0, round(self.explosionForce / 1.5)))
            self.childrenParticlesList.append(FireworkParticles(self.timeToSleep, self.window, self.YSize, self.XSize, self.XPos, self.YPos, 0, round(-self.explosionForce / 1.5)))
                    
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

    # fireworksList.append(Firework(timeToSleep, window, YSize, XSize))

    # for i in range(1000):
    while True:
        createBall = rndm.randint(0, 20)
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