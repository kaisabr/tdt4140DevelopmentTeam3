class carInput():

    def __init__(self):
        file = open('speeds.txt', 'r')
        textFromFile = file.read()
        self.speeds = textFromFile.split('\n')

    def getCurrentSpeed(self):
        while len(self.speeds) != 0:
            return self.speeds.pop(0)

    def getIsInteriorLightOn(a):
        pass

    # print isInteriorLightOn(1)

    #Returns distance to object to the left side of the car. Method returns distance in meters. Used by VAR4. Written by Katharina and Magnus.
    def distanceToLeftSide(self):
        pass

    #Returns distance to object to the right side of the car. Method returns distance in meters. Used by VAR4. Written by Katharina and Magnus.
    def distanceToRightSide(self):
        pass

    #Returns whether left indicator light is on. Method returns answer in boolean. Used by VAR4. Written by Katharina and Magnus.
    def leftIndicatorLightIsOn(self):
        pass

    #Returns whether right indicator light is on. Method returns answer in boolean. Used by VAR4. Written by Katharina and Magnus.
    def rightIndicatorLightIsOn(self):
        pass

    def getDistanceToCarAhead(self):
        pass

    def isCarOn(self, carSignal):
        if carSignal == 1:
            return True
        else:
            return False

    # Should check if switch for indicator light is activated
    def indicatorLightSwitchedOn(self, lightSignal):
        if lightSignal == 1:
            return True
        else:
            return False

    # Should check if brakes are used
    def brakePushed(self, brakeSignal):
        if brakeSignal == 1:
            return True
        else:
            return False

    # The method checks if the ligthsensor recieves input. Returns False if everything is OK.
    # sensorInput recieves either a 0, if the light is not on, and 1 if the light is on.
    def isLightOff(self, sensorInput):
        if sensorInput == 0:
            return True
        else:
            return False
