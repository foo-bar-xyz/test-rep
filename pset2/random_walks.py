# Location - a place
# Field - a collection of places and drunks
# Drunks - somebody who wanders from place to place in a Field
#    UsualDrunk
#    ColdDrunk go to south

import random

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def dist_from(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Dublicate drunk')
        else:
            self.drunks[drunk] = loc

    def get_loc(self, drunk):
        if drunk not in self.drunks:
            raise ValuError('Drunk not in field')
        return self.drunks[drunk]

    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.take_step()
        currentLocation =  self.drunks[drunk]
        #use move method of Location class  to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
    def take_step(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def take_step(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

################################################################################

def walk(f, d, numSteps):
    """
        Assumes:
                f - a Field
                d - a Drunk in f
                numSteps - int >= 0
                Moves d numSteps times
                returns the distance between the final
                location and the location at the start of the walk.
    """
    start = f.get_loc(d)
    for s in range(numSteps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))

def sim_walks(numSteps, numTrials, dClass):
    """
        Assumes:
            numSteps - int >= 0
            numTrials - int > 0
            dClass - a subclass of Drunk
        Simulates numTrials walks of numSteps steps each
        Returns a list of the final distances for each trial
    """
    Homer = dClass('Homer')
    origin = Location(0.0, 0.0)
    distances = []
    for t in range(numTrials):
        f =Field()
        f.add_drunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances

def drunk_test(walkLengths, numTrials, dClass):
    """
        Assumes
            walkLength a sequence of ints >= 0
            numTrials an int > 0
            dClass a subclass of Drunk
        For each number of steps in walkLengths, runs sim_walks with numTrials
        walks and prints results
    """
    for numSteps in walkLengths:
        distances = sim_walks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', str(numSteps), 'steps')
        print('Mean =', round(sum(distances) / len(distances), 4))
        print('Max =', max(distances))
        print('Min =', min(distances))

def sim_all(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunk_test(walkLengths, numTrials, dClass)

random.seed(0)
sim_all((UsualDrunk, ColdDrunk), (10, 100, 1000, 10000), 100)
#drunk_test((10, 100, 1000, 10000), 100, UsualDrunk)
#drunk_test((0, 1, 2), 100, UsualDrunk)
