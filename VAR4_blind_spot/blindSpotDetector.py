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

    #Returns distance to object to the left side of the car. Method returns distance in meters. Written by Katharina and Magnus.
    def distanceToLeftSide(self):
        pass

    #Returns distance to object to the right side of the car. Method returns distance in meters. Written by Katharina and Magnus.
    def distanceToRightSide(self):
        pass

    #Returns whether left indicator light is on. Method returns answer in boolean. Written by Katharina and Magnus.
    def leftIndicatorLightIsOn(self):
        pass

    #Returns whether right indicator light is on. Method returns answer in boolean. Written by Katharina and Magnus.
    def rightIndicatorLightIsOn(self):
        pass
