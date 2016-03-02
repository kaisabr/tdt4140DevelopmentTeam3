from itertools import izip

constant = 1.1
#En fil med speedlimit
speedLimit = 'SpeedLimit.txt'
#en fil med current speed
speed = 'Speed.txt'

class SpeedLimit():

    def openFile(self, mySpeed, speedLimit):
        with open(mySpeed, 'r') as speedInput, open(speedLimit, 'r') as speedLimitInput:
            # speedInputLine = speedInput.readlines()
            # speedLimitInputLine = speedLimitInput.readlines()

            for speedLine, speedLimitLine in izip(speedInput, speedLimitInput):
                speedLine, speedLimitLine = int(speedLine.split("\t")[0]), int(speedLimitLine.split("\t")[0])

                if (speedLine == '' or speedLimitLine == ''):
                    return None
                else:
                    x = speedLine
                    y = speedLimitLine

                    if x <= (y*constant):
                        return True
                    else:
                        return False, self.sound()


        speedInput.close()
        speedLimitInput.close()

            # for s, p in izip(xrange(len(speedInputLine)), xrange(len(speedLimitInputLine))):
            #     if (speedInputLine[s] == '' or speedLimitInputLine[p] == ''):
            #         return None
            #     else:
            #         x = int(speedInputLine[s].strip())
            #         y = int(speedLimitInputLine[p].strip())
            #
            #         if x <= (y*constant):
            #             return True
            #         else:
            #             return False and self.sound()

    # def drivingOK(self, mySpeed, speedLimit):
    #     #file_opened = int(speedLimit().openFile(mySpeed, speedLimit)
    #
    #     speed = SpeedLimit().openFile(mySpeed, speedLimit)[0]
    #     speedLimit = SpeedLimit().openFile(mySpeed, speedLimit)[1]

    def sound(self):
        return "Pip"


sp = SpeedLimit()
print sp.openFile(speed, speedLimit)
