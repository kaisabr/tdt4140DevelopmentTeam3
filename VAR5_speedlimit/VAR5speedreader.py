from itertools import izip

constant = 1.1

class SpeedLimit():

    def drivingOK(self, mySpeed, speedLimit):
        if mySpeed <= (speedLimit*constant):
            return True
        else:
            return False
        # for x in range(len(mySpeed)):
        #     if mySpeed[x] <= (speedLimit*constant):
        #         return True
        #     else:
        #         return False

    def drivingToFast(self, myspeed, speedLimit):
        if (myspeed <= (speedLimit*constant)):
            return False
        else:
            return True


    with open("Speed.txt") as speedInput, open("SpeedLimit.txt") as speedLimitInput:
        for lineInSpeedInput, lineInSpeedLimitInput in izip(speedInput, speedLimitInput):
            x = lineInSpeedInput.strip()
            y = lineInSpeedLimitInput.strip()
            print "{0}\t{1}".format(x, y)

            if drivingOK(x, y):
                print "OK"
            if drivingToFast(x, y):
                print "Driving to Fast"