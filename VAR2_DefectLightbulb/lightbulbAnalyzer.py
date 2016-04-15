# ARNA AND MAREN

"""
USER STORY

As a user
I want to be notified if any lights do not work
So I can change bulbs

"""

from siren import *

class lightBulbAnalyzer:

    def __init__(self, car, siren):
        self.car = car
        self.siren = siren

# Checks if the front light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isFrontLightOff(self):
        defectFront = self.car.isLightOff()
        if defectFront == True and self.car.carIsOn():
            self.siren.triggeredByVAR2("Front ligth is not on. Make sure it is working")

# Checks if the back light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isBackLightOff(self):
        defectBack = self.car.isLightOff()
        if defectBack == True and self.car.carIsOn():
            self.siren.triggeredByVAR2("Back ligth is not on. Make sure it is working")

# Checks if the licence plate light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isLicencePlateLightOff(self):
        defectLP = self.car.isLightOff()
        if defectLP == True and self.car.carIsOn():
            self.siren.triggeredByVAR2("Licence plate ligth is not on. Make sure it is working")

# Checks if it gets input from indicator light sensor when switch for indicator light is activated.
# If no response is given after 5 seconds, a warning message is given
    def isIndicatorLightOff(self):
        off = 0
        on = 0
        if self.car.carIsOn() and self.car.indicatorLightSwitchedOn():
            for x in range(0, 5):
                if self.car.isLightOff() == True:
                    off += 1
                else:
                    on += 1
            if off == 5:
                self.siren("Please check your indicator light. No input to light sensor for 5 seconds")

# Checks if brake light is on when car is on and brakes and brakes are pushed. Warning message given if it is not.
    def isBrakeLightOn(self):
        if self.car.carIsOn() and self.car.brakePushed():
            if self.car.isLightOff():
                self.siren.triggeredByVAR2("Brake light is not on. Make sure it is working")
