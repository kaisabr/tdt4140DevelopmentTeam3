

class speedLimit():

    speedLimit = 80
    speed = [30, 45, 69, 88, 30, 72, 100]
    constant = 1.1

    def drivingToFast(self, speed, speedlimit):
        if(speed > (speedLimit*self.constant)):
