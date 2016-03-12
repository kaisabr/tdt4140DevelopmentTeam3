class carInput():

    def currentSpeed(self):
        speeds = open('speedFile.txt','r')
        for line in speeds:
            if line.strip() == "\n":
                pass
            speed = int(line.strip())
            if speed <0:
                pass
            else:
                return speed

    def isInteriorLightOn(a):
        pass



    print isInteriorLightOn(1)


    def distanceToCar(self):
        pass

    def carIsOn(self):
        pass

    #Returns distance to object to the left side of the car. Method returns distance in meters. Written by Katharina and Magnus.
    def distanceToLeftSide(self):
        pass

    #Returns distance to object to the right side of the car. Method returns distance in meters. Written by Katharina and Magnus.
    def distanceToRightSide(self):
        pass

    #Returns whether left indicator light is on. Method returns answer in boolean. Written by Katharina and Magnus.
    def leftIndicatorLightIsOn(self):
        pass

    #Returns whether right indicator light is on. Method returns answer in boolean. Written by Katharina and Magnus.
    def rightIndicatorLightIsOn(self):
        pass

    #Should check if switch for indicator light is activated
    def IndicatorLightSwitchedOn(self):
        pass

#Should check if brakes are used
    def brakePushed(self):
        pass

    #The method checks if the ligthsensor recieves input. Returns False if everything is OK.
    #sensorInput recieves either a 0, if the light is not on, and 1 if the light is on.
    def isLightOff(self, sensorInput):
        if sensorInput == 0:
            return True
        return False


