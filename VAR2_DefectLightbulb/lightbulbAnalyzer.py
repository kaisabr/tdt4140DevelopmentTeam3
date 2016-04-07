# ARNA AND MAREN

"""
USER STORY

As a user
I want to be notified if any lights does not work
So I can change the bulbs

"""

from carInput import *


class lightBulbAnalyzer:

# Checks if the front light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isFrontLightOff(self, frontLightSensor, carSignal):
        defectFront = carInput().isLightOff(frontLightSensor)
        if defectFront == True and carInput().carIsOn(carSignal):
            return "Front ligth is not on. Make sure it is working"

# Checks if the back light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isBackLightOff(self, backLightSensor, carSignal):
        defectBack = carInput().isLightOff(backLightSensor)
        if defectBack == True and carInput().carIsOn(carSignal):
            return "Back ligth is not on. Make sure it is working"

# Checks if the licence plate light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isLicencePlateLightOff(self, licensePlateLightSensor, carSignal):
        defectLP = carInput().isLightOff(licensePlateLightSensor)
        if defectLP == True and carInput().carIsOn(carSignal):
            return "Licence plate ligth is not on. Make sure it is working"

# Checks if it gets input from indicator light sensor when switch for indicator light is activated.
# If no response is given after 5 seconds, a warning message is given
    def isIndicatorLightOff(self, indicatorLightSensor, carSignal, switchedOn):
        off = 0
        on = 0
        if carInput().carIsOn(carSignal) and carInput().indicatorLightSwitchedOn(switchedOn):
            for x in range(0, 5):
                if carInput().isLightOff(indicatorLightSensor) == True:
                    off += 1
                else:
                    on += 1
            if off == 5:
                return "Please check your indicator light. No input to light sensor for 5 seconds"

# Checks if brake light is on when car is on and brakes and brakes are pushed. Warning message given if it is not.
    def isBrakeLightOn(self, carSignal, brakeSignal, lightSensor):
        if carInput().carIsOn(carSignal) and carInput().brakePushed(brakeSignal):
            if carInput().isLightOff(lightSensor):
                return "Brake light is not on. Make sure it is working"
