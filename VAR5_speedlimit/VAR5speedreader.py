from itertools import izip

constant = 1.1
#En fil med speedlimit
speedLimit = 'SpeedLimit.txt'
#en fil med current speed
speed = 'Speed.txt'

class SpeedLimit():

    def openFile(self, mySpeed, speedLimit):
        with open(mySpeed, 'r') as speedInput, open(speedLimit, 'r') as speedLimitInput:
            # speedInputLine = [next(speedInput) for x in xrange(SpeedLimit().countLines(mySpeed))]
            # speedLimitInputLine = [next(speedLimitInput) for y in xrange(SpeedLimit().countLines(speedLimit))]
            speedInputLine = speedInput.readlines()
            speedLimitInputLine = speedLimitInput.readlines()

            for s, p in izip(xrange(len(speedInputLine)), xrange(len(speedLimitInputLine))):
                if (speedInputLine[s] == '' or speedLimitInputLine[p] == ''):
                # if (speedInputLine == '' or speedLimitInputLine == ''):
                    return None
                else:
                    x = int(speedInputLine[s].strip())
                    y = int(speedLimitInputLine[p].strip())

                    if x <= (y*constant):
                        return True
                    else:
                        return False and self.sound()

    # def drivingOK(self, mySpeed, speedLimit):
    #     #file_opened = int(speedLimit().openFile(mySpeed, speedLimit)
    #
    #     speed = SpeedLimit().openFile(mySpeed, speedLimit)[0]
    #     speedLimit = SpeedLimit().openFile(mySpeed, speedLimit)[1]

    def sound(self):
        return "Pip" and "hei"

    def countLines(self, file):
        with open(file) as f:
            for i, l in enumerate(f):
                pass
        return i + 1


sp = SpeedLimit()
print sp.openFile(speed, speedLimit)
