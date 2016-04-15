from siren import siren

class blindSpotDetector():

    def __init__(self, car):
        self.car = car

    def main(self):
        if self.tooCloseToLeftSide():
            siren().triggeredByDistanceToSide()
        elif self.tooCloseToRightSide():
            siren().triggeredByDistanceToSide()

    def tooCloseToLeftSide(self):
        distance = self.car.distanceToLeftSide()
        lightIsOn = self.car.leftIndicatorLightIsOn()

        if float(distance) < 2.5 and lightIsOn:
            return True
        else:
            return False

    def tooCloseToRightSide(self):
        distance = self.car.distanceToLeftSide()
        lightIsOn = self.car.leftIndicatorLightIsOn()

        if float(distance) < 2.5 and lightIsOn:
            return True
        else:
            return False