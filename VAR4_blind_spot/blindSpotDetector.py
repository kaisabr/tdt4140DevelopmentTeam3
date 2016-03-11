import carInput

class blindSpotDetector():

    def main(self):
        if tooCloseToLeftSide():
            siren().triggeredByDistanceToSide()
        if tooCloseToRightSide():
            siren().triggeredByDistanceToSide()

    def tooCloseToLeftSide(self):
        distance = distanceToLeftSide()
        lightIsOn = leftIndicatorLightIsOn()

        if distance < 2.5 & lightIsOn:
            return True

    def tooCloseToRightSide(self):
        distance = distanceToLeftSide()
        lightIsOn = leftIndicatorLightIsOn()

        if distance < 2.5 & lightIsOn:
            return True;
