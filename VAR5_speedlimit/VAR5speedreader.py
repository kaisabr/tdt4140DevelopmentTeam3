# ARNA, MAREN and MATHILDE

"""
USER STORY

As a user
I want to be notified when driving over 1.1*the speed limit
So I can avoid getting fined

"""


from itertools import izip
from siren import *

constant = 1.1

class SpeedLimit:

    def __init__(self, car, siren):
        self.car = car
        self.siren = siren

    # Open file
    def checkSpeed(self, mySpeed, speedLimit):
        with open(mySpeed, 'r') as speedInput, open(speedLimit, 'r') as speedLimitInput:
            # Iterating over the two files, one for speed and one for speed limit
            for speedLine, speedLimitLine in izip(speedInput, speedLimitInput):
                # converting to int
                speedLine, speedLimitLine = int(speedLine.split("\t")[0]), int(speedLimitLine.split("\t")[0])

                # Check if there is no empty line
                if (speedLine == '' or speedLimitLine == ''):
                    return None
                else:
                    x = speedLine
                    y = speedLimitLine

                    # checking speed
                    if x <= (y*constant):
                        return True
                    else:
                        self.siren.triggeredByVAR15()
                        return False
        # closing files
        speedInput.close()
        speedLimitInput.close()

# sp = SpeedLimit()
# print sp.openFile(speed, speedLimit)
