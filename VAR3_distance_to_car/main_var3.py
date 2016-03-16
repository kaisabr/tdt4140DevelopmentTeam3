# Skrevet av Magnus og Aashild

import siren
import carInput

class distanceAnalyzer():

    # Beregner optimal distanse.
    def calculateOptimalDistance(self):
        speed = carInput.getSpeed()
        return speed*3

    # Sirenen varsler dersom avstanden til bilen foran er for liten
    def calculateIfTooCloseToCar(self):
        speed = carInput.getSpeed()
        distance = carInput.distanceToCarAhead()
        carIsOn = carInput.carIsOn()
        while carIsOn:
            if self.calculateOptimalDistance() > distance:
                siren.triggeredByDistanceToCar()
            else:
                continue
