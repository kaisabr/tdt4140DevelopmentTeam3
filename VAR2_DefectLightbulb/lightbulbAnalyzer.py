from carInput import *


class lightBulbAnalyzer:

#Checks if the front light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isFrontLightOff(self, frontLightSensor):
        defectFront = carInput.isLightOff(self, frontLightSensor)
        if defectFront == True and carInput.carIsOn(self):
            return "Front ligth is not on. Make sure it is working"

#Checks if the back light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isBackLightOff(self, backLightSensor):
        defectBack = carInput.isLightOff(self, backLightSensor)
        if defectBack == True and carInput.carIsOn(self):
            return "Back ligth is not on. Make sure it is working"

#Checks if the licence plate light sensor gets input when the car is on. Returns a message to check light if it is not.
    def isLicencePlateLightOff(self, licensePlateLightSensor):
        defectLP = carInput.isLightOff(self, licensePlateLightSensor)
        if defectLP == True and carInput.carIsOn(self):
            return "Licence plate ligth is not on. Make sure it is working"

#Checks if it gets input from indicator light sensor when switch for indicator light is activated.
#If no response is given after 5 seconds, a warning message is given
    def isIndicatorLightOff(self, indicatorLightSensor):
        off = 0
        on = 0
        if carInput.carIsOn(self) and carInput.indicatorLightSwitchedOn(self):
            for x in range(0,4):
                if carInput.isLightOff(self, indicatorLightSensor) == True:
                    off += 1
                else:
                    on += 1
            if off == 5:
                return "Please check your indicator light. No input to light sensor for 5 seconds"

#Checks if brake light is on when car is on and brakes and brakes are pushed. Warning message given if it is not.
    def isBrakeLightOn(self, brakeLightSensor):
        if carInput.carIsOn(self) and carInput.brakePushed(self):
            if carInput.isLightOff(self, brakeLightSensor):
                return "Brake light is not on. Make sure it is working"
