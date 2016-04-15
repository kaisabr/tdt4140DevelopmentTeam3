from siren import siren

class blindSpotDetector():

    def __init__(self, car, siren):
        self.car = car
        self.siren = siren

    def main(self):
        if self.tooCloseToLeftSide():
            self.siren.triggeredByVAR4()
        elif self.tooCloseToRightSide():
            self.siren.triggeredByVAR4()

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