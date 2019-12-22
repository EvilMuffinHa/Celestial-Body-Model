from math import *


#Orbiter objects
class Orbiter:
    _orbiters = []
    #Initialize the Orbiter object with its values
    def __init__(self, mass, position, velocity, name, color, scale):
        self.mass = mass
        self.px = position[0]
        self.py = position[1]
        self.vy = velocity[0]
        self.vx = velocity[1]
        self.color = color
        self.__doc__ = name
        self.scale = scale
        Orbiter._orbiters.append(self)


    # Args - [(xpoint, ypoint, mass), (xpoint, ypoint, mass)]
    #Force of gravity
    def GetFgXY(self, *args):
        self.netgx = 0
        self.netgy = 0
        for i in args[0]:
            dist = sqrt((i[0] - self.px)**2 + (i[1] - self.py)**2)
            disty = self.py - i[1]
            distx = self.px - i[0]
            fgx = ((6.67*10**-11) * i[2])/(dist**2)
            self.netgy -= fgx/dist * disty
            self.netgx -= fgx/dist * distx


    #Retrieving information about that specific object
    def GetInfo(self):
        print('-' * 50)
        print('Object: ' + self.__doc__)
        print('Mass: ' + str(self.mass))
        print('X Position: ' + str(self.px))
        print('Y Position: ' + str(self.py))
        print('X Velocity: ' + str(self.vx))
        print('Y Velocity: ' + str(self.vy))
        print('-' * 50)

    #Getting more information about that object (only works after at least 1 run of GetFgXY()
    def GetExtendedInfo(self):
        print('-' * 50)
        print('Object: ' + self.__doc__)
        print('Mass: ' + str(self.mass))
        print('X Position: ' + str(self.px))
        print('Y Position: ' + str(self.py))
        print('X Velocity: ' + str(self.vx))
        print('Y Velocity: ' + str(self.vy))
        print('X Acceleration: ' + str(self.netgx/self.mass))
        print('Y Acceleration: ' + str(self.netgy/self.mass))
        print('Orbiters in the system: ' + ', '.join([x.__doc__ for x in Orbiter._orbiters]))
        print('-' * 50)
