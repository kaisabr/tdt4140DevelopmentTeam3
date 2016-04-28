# ARNA, MAREN and MATHILDE

"""
USER STORY

As a user
I want to be notified when driving over 1.1*the speed limit
So I can avoid getting fined

"""


from itertools import izip
from siren import *
from carInput import *

constant = 1.1

class SpeedLimit:

    def __init__(self, car, siren):
        self.car = car
        self.siren = siren

    # Open file
    def checkSpeed(self):
        x = float(self.car.getCurrentSpeed())
        y = float(self.car.getSpeedLimit())

        # checking speed
        if x <= (y*constant):
            return True
        else:
            self.siren.triggeredByVAR5()
            return False
