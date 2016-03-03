from itertools import izip

constant = 1.1

class SpeedLimit():

    def openFile(self, mySpeed, speedLimit):
        with open(mySpeed, 'r') as speedInput, open(speedLimit, 'r') as speedLimitInput:

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
                        self.sound()
                        return False

        speedInput.close()
        speedLimitInput.close()

    def sound(self):
        return "Pip"

# sp = SpeedLimit()
# print sp.openFile(speed, speedLimit)
