from random import randint
from random import uniform
from random import random
import numpy as np


class People:
    def __init__(self, x, y, who, sdist, xlim=(0, 100), ylim=(0, 100), attraction=0.5, infected=0, step=1):
        self.x = x
        self.y = y
        self.xpre = x
        self.ypre = y
        self.who = who
        self.sdist = sdist
        self.xlim = xlim
        self.ylim = ylim
        self.attraction = attraction
        self.infected = infected
        self.distance = []
        self.step = step
        self.xdir, self.ydir = (0, 0)
        self.momentum = 0.8

        if self.infected == 1:
            self.marker = "x"
            self.color = "C1"
        else:
            self.marker = "o"
            self.color = "C0"

    def random_step(self, curpos):
        # Momentum
        if random() > self.momentum:
            #self.xdir = randint(-self.step, self.step)
            #self.ydir = randint(-self.step, self.step)
            self.xdir = uniform(-self.step, self.step)
            self.ydir = uniform(-self.step, self.step)

        tempx = self.x + self.xdir
        tempy = self.y + self.ydir

        if not (tempx < self.xlim[0] or tempx > self.xlim[1]):
            self.x = tempx

        if not (tempy < self.ylim[0] or tempy > self.ylim[1]):
            self.y = tempy

        # Get the distance from all agents in the space
        a = np.array([self.x, self.y])
        self.distance = [(who, np.linalg.norm(a - np.array([p[0], p[1]])), (p[0], p[1])) for who, p in enumerate(curpos)]
        self.distance.sort(key=lambda x: x[1])

        return self.distance

    def avoidance_step(self, curpos):
        # Update the previous steps
        self.xpre = self.x
        self.ypre = self.y

        # Get the distance from all agents in the space
        a = np.array([self.x, self.y])
        self.distance = [(who, np.linalg.norm(a - np.array([p[0], p[1]])), (p[0], p[1])) for who, p in enumerate(curpos)]
        self.distance.sort(key=lambda x: x[1])

        # Define the stepdir() function which finds the direction to maximize distance amongst close agents
        def stepdir(distance, who, step):
            maxr = 20
            closest = [d for d in distance if d[1] <= maxr]
            xavg = np.mean([x[2][0] for x in closest if x[0] != who])
            yavg = np.mean([y[2][1] for y in closest if y[0] != who])
            a = np.array(closest[0][2])
            b = np.array([xavg, yavg])
            direc = (a - b) / np.linalg.norm(a-b)
            direc *= step * uniform(0, 1)

            return direc

        # Determine if they should step away or take a random step
        if self.distance[1][1] <= self.sdist + 3:
            direction = stepdir(self.distance, self.who, self.step)
            self.xdir = direction[0]
            self.ydir = direction[1]

            tempx = self.x + self.xdir
            tempy = self.y + self.ydir

            """
            # Update xpos
            if self.distance[1][2][0] < 0:
                self.xdir = uniform(0, self.step)
                tempx = self.xpre + self.xdir
            else:
                self.xdir = uniform(-self.step, 0)
                tempx = self.xpre + self.xdir

            # Update ypos
            if self.distance[1][2][1] < 0:
                self.ydir = uniform(0, self.step)
                tempy = self.ypre + self.ydir
            else:
                self.ydir = uniform(-self.step, 0)
                tempy = self.ypre + self.ydir
            """
        else:
            # Momentum
            if random() > self.momentum:
                self.xdir = uniform(-self.step, self.step)
                self.ydir = uniform(-self.step, self.step)

            tempx = self.xpre + self.xdir
            tempy = self.ypre + self.ydir

        # Only update the position if they are still within the limit of the space
        if not (tempx < self.xlim[0] or tempx > self.xlim[1]):
            self.x = tempx

        if not (tempy < self.ylim[0] or tempy > self.ylim[1]):
            self.y = tempy

        return self.distance

    def contracted(self, infected):
        assert type(infected) == int, "ERROR: 'infected' must be an int of 0 or 1"
        self.infected = infected

        if self.infected == 1:
            self.marker = "x"
            self.color = "C1"

        else:
            self.marker = "o"
            self.color = "C0"
