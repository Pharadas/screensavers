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
        # if self.YSpeed > -5:
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
            # else:
            #     self.delete = True

        # else: 
        #     self.exploded = True
        #     movelength = self.explosionForce / self.amountOfParticles
        #     side = self.explosionForce / 2
        #     for i in range(self.amountOfParticles + 1):
        #         rest = (self.explosionForce ** 2) - (round(side) ** 2)
        #         if rest != 0:
        #             YParticleSpeed = math.sqrt(rest)
        #         self.childrenParticlesList.append(FireworkParticles(self.timeToSleep, self.window, self.YSize, self.XSize, self.XPos, self.YPos, self.explosionHorizontalForce, xparticleSpeed + self.XSpeed)
        #         # window.addstr(self.init_posY + 1, init_posX + round(side), '1')
        #         side -= movelength
                    
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
        # for firework in fireworksList:
        #     firework.move()
        #     ballsdict[ball]['Yspeed'] -= ballsdict[ball]['gravity'] * timeToSleep
        #     ballsdict[ball]['realPosX'] += ballsdict[ball]['Xspeed'] * timeToSleep
        #     ballsdict[ball]['realPosY'] -= ballsdict[ball]['Yspeed'] * timeToSleep
        #     ballsdict[ball]['posX'] = int(ballsdict[ball]['realPosX'])
        #     ballsdict[ball]['posY'] = int(ballsdict[ball]['realPosY'])

        #     if not ballsdict[ball]['firework?']:
        #         if ballsdict[ball]['posY'] < YSize:
        #             if ballsdict[ball]['posY'] > 0:
        #                 try:
        #                     window.addstr(ballsdict[ball]['posY'], ballsdict[ball]['posX'], '0')
        #                 except:
        #                     ballsdict[ball]['Xspeed'] = ballsdict[ball]['Xspeed'] * -1 
        #             if ballsdict[ball]['Yspeed'] < -1:
        #                 ballsdict[ball]['firework?'] = True
        #                 val = 5
        #                 direction = -val
        #                 for i in range(val * 2):
        #                     ballsdict[ball]['firework_particles'][len(ballsdict[ball]['firework_particles']) + 1] = {
        #                         'Xspeed': direction, 
        #                         'Yspeed': 5, 
        #                         'gravity': 9.81, # -(rndm.randint(1, 2)), 
        #                         'posX': ballsdict[ball]['posX'], # [rndm.randint(0, XSize - 1), YSize]
        #                         'posY': ballsdict[ball]['posY'], # [rndm.randint(0, XSize - 1), YSize]
        #                         'realPosX': ballsdict[ball]['posX'],
        #                         'realPosY': ballsdict[ball]['posY'],
        #                         }
        #                     direction += 1
        #         else:
        #             ballsToDelete.append(ball)
        #     else:
        #         for firework_particle in ballsdict[ball]['firework_particles']:
        #             ballsdict[ball]['firework_particles'][firework_particle]['Yspeed'] -= ballsdict[ball]['firework_particles'][firework_particle]['gravity'] * timeToSleep
        #             ballsdict[ball]['firework_particles'][firework_particle]['Yspeed']

        #             ballsdict[ball]['realPosX'] += ballsdict[ball]['Xspeed'] * timeToSleep
        #             ballsdict[ball]['realPosY'] -= ballsdict[ball]['Yspeed'] * timeToSleep
        #             ballsdict[ball]['posX'] = int(ballsdict[ball]['realPosX'])
        #             ballsdict[ball]['posY'] = int(ballsdict[ball]['realPosY'])

        # for i in ballsToDelete:
        #     del i

curses.wrapper(pbar)

# python C:\Users\David\Documents\Repos\PythonRepos\screensaver\gravityballs.py