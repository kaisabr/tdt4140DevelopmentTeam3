#class for interior light
import carInput

class interiorLightAnalyzer:
    #Method returns the speeds in 0s and 1s
    def convertSpeed(self, speed):
        if speed != 0:
            return 1
        else:
            return 0

    def getInteriorLightStatus(self):
        light = open('sensorForInteriorLightData.txt', 'r') #sensorForInteriorLightData is a fil with 0s and 1s
        for line in light:
            return int(line.strip())

        
    #the method returns flase if everything is OK (no notifications), if not, it returns false
    def interiorLightCheck(self, d): #take in value for light, door and speed (1 or 0)
        speed = carInput.getSpeed()
        l = interiorLightAnalyzer.getInteriorLightStatus()
        while speed and l:
            s = interiorLightAnalyzer.convertSpeed(speed)
            if l == 1 and d == 0 and s == 0: #the only time it is ok for the light to be on
                return False
                #siren = Siren.siren(False)
            elif l==1: #light is on, but dor is open or/and the car has a speed
                return True
                #siren = Siren.siren(True)
            else:
                return False #the light is off, no notification necessary
                #siren = Siren.siren(False)
