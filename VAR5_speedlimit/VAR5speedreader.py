

currentSpeedLimit = 80
speed = [30, 45, 69, 88, 30, 72, 1000]
constant = 1.1

class speedLimit():

    def drivingToFast(self, mySpeed, speedLimit):

        for x in range(len(mySpeed)):
            if(mySpeed[x] <= (speedLimit*constant)):
                print "OK"
            else:
                print "Driving to fast"


testSpeed = speedLimit()
testSpeed.drivingToFast(speed, currentSpeedLimit)
