constant = 1.1

class SpeedLimit():

    def drivingOK(self, mySpeed, speedLimit):
         for x in range(len(mySpeed)):
             if mySpeed[x] <= (speedLimit*constant):
                 return True
             else:
                 return False

    def drivingToFast(self, myspeed, fartsgrense):
        if (myspeed <= (fartsgrense*constant)):
            return False
        else:
            return True