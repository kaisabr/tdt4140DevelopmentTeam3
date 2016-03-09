class carInput():
    
    def getSpeed(self, speedFile):
        speeds = open(speedFile, 'r')
        for line in speeds: # For hver linje i inputfilen (som inneholder en fart per linje)
            speed = int(line.strip())
            if speed < 0:
                pass
            else:
                return speed # returnerer en int med farten (som endrer seg kontinuerlig).

    def isInteriorLightOn(self):
        pass

    def distanceToCar(self):
        pass

def openFile(file):
    pass