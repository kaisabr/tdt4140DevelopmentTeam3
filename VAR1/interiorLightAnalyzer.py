
#class for interior light
from siren import*

class interiorLightAnalyzer():

    def __init__(self, car, siren):
        self.car = car
        self.siren = siren

    #Method returns the speeds in 0s and 1s
    def convertSpeed(self, speed):
        if speed != 0:
            return 1
        else:
            return 0


        
    #the method returns flase if everything is OK (no notifications), if not, it returns false
    def interiorLightCheck(self): #take in value for light, door and speed (1 or 0)

        speed = self.car.getCurrentSpeed()
        light = self.car.isInteriorLightOn()
        door = self.car.isDoorOpen()

        sjekk = False
        s = interiorLightAnalyzer.convertSpeed(self,int(speed))
        if light == '1' and door == '0' and s == 0: #the only time it is ok for the light to be on
            sjekk= False
            #siren = Siren.siren(False)
        elif light=='1': #light is on, but dor is open or/and the car has a speed
            sjekk= True
            #siren = Siren.siren(True)
        else:
            sjekk= False #the light is off, no notification necessary
            #siren = Siren.siren(False)

        if sjekk == True and sjekk != None:
            self.siren.triggeredByVAR1()