import winsound

class siren():

    def __init__(self):
        pass

    def triggeredByInteriorLight(self):
        print "Check if your interior light is on"

    def triggeredByDistanceToCarInFront(self):

        print "Distance to car in front is too small."

    def triggeredByDistanceToCar(self):
        pass

    def triggeredByDistanceToSide(self):
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print "There is an object in your blind spot."

