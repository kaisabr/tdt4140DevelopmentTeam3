# Skrevet av Magnus og Aashild

from siren import siren

class distanceAnalyzer():

    def __init__(self, car):
        self.car = car

    # Beregner optimal distanse.
    def calculateOptimalDistance(self):
        speed = self.car.getCurrentSpeed()
        return speed*3

    # Sirenen varsler dersom avstanden til bilen foran er for liten
    def calculateIfTooCloseToCar(self):
        distance = self.car.distanceToCar()
        carOn = self.car.carIsOn()
        if carOn:
            if self.calculateOptimalDistance() > distance:
                siren.triggeredByDistanceToCarInFront()
