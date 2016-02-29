import mailbox

#currentSpeedLimit = 80
#speed = 66
constant = 1.1


class speedLimit():

    # def drivingToFast(self, mySpeed, speedLimit):
    #     for x in range(len(mySpeed)):
    #         if(mySpeed[x] <= (speedLimit*constant)):
    #             print "OK"
    #         else:
    #             print "Driving to fast"

    def drivingToFast2(self, myspeed, fartsgrense):
        if myspeed <= (fartsgrense*constant):
            print "OK"
        else:
            print "Driving to fast"


# if __name__ == '__main__':
#     speed = speedLimit()
#     speed.drivingToFast2(90, 80)