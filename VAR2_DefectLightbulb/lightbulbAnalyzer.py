# ARNA AND MAREN

"""
USER STORY

As a user
I want to be notified if any lights do not work
So I can change bulbs

"""


class lightBulbAnalyzer:

    def __init__(self, car):
        self.car = car

# Checks if the front light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isFrontLightOff(self, frontLightSensor, carSignal):
        defectFront = self.car.isLightOff(frontLightSensor)
        if defectFront == True and self.car.carIsOn(carSignal):
            return "Front ligth is not on. Make sure it is working"

# Checks if the back light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isBackLightOff(self, backLightSensor, carSignal):
        defectBack = self.car.isLightOff(backLightSensor)
        if defectBack == True and self.car.carIsOn(carSignal):
            return "Back ligth is not on. Make sure it is working"

# Checks if the licence plate light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isLicencePlateLightOff(self, licensePlateLightSensor, carSignal):
        defectLP = self.car.isLightOff(licensePlateLightSensor)
        if defectLP == True and self.car.carIsOn(carSignal):
            return "Licence plate ligth is not on. Make sure it is working"

# Checks if it gets input from indicator light sensor when switch for indicator light is activated.
# If no response is given after 5 seconds, a warning message is given
    def isIndicatorLightOff(self, indicatorLightSensor, carSignal, switchedOn):
        off = 0
        on = 0
        if self.car.carIsOn(carSignal) and self.car.indicatorLightSwitchedOn(switchedOn):
            for x in range(0, 5):
                if self.car.isLightOff(indicatorLightSensor) == True:
                    off += 1
                else:
                    on += 1
            if off == 5:
                return "Please check your indicator light. No input to light sensor for 5 seconds"

# Checks if brake light is on when car is on and brakes and brakes are pushed. Warning message given if it is not.
    def isBrakeLightOn(self, carSignal, brakeSignal, lightSensor):
        if self.car.carIsOn(carSignal) and self.car.brakePushed(brakeSignal):
            if self.car.isLightOff(lightSensor):
                return "Brake light is not on. Make sure it is working"
