# Skrevet av Magnus og Aashild

from siren import siren

class distanceAnalyzer():

    def __init__(self, car, siren):
        self.car = car
        self.siren = siren

    # Beregner optimal distanse.
    def calculateOptimalDistance(self):
        speed = self.car.getCurrentSpeed()
        speed = float(speed)
        speed = speed/3.6
        return speed*3

    # Sirenen varsler dersom avstanden til bilen foran er for liten
    def calculateIfTooCloseToCar(self):
        distance = self.car.distanceToCar()
        carOn = self.car.carIsOn()
        if carOn:
            if self.calculateOptimalDistance() > distance:
                self.siren.triggeredByVAR3()
