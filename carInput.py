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

    def isInteriorLightOn(self):
        pass

    def distanceToCar(self):
        pass

    def carIsOn(self):
        pass



