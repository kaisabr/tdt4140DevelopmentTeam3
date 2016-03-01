constant = 1.1

class SpeedLimit():

    def drivingOK(self, mySpeed, speedLimit):
         for x in range(len(mySpeed)):
             if mySpeed[x] <= (speedLimit*constant):
                 return True
             else:
                 return False

    def drivingToFast(self, myspeed, speedLimit):
        if (myspeed <= (speedLimit*constant)):
            return False
        else:
            return True