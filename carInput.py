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


