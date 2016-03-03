from itertools import izip

constant = 1.1

class SpeedLimit():

    countTrue = 0
    countFalse = 0

    lineCounter = 0

    def openFile(self, mySpeed, speedLimit):
        with open(mySpeed, 'r') as speedInput, open(speedLimit, 'r') as speedLimitInput:

            for speedLine, speedLimitLine in izip(speedInput, speedLimitInput):
                speedLine, speedLimitLine = int(speedLine.split("\t")[0]), int(speedLimitLine.split("\t")[0])

                if (speedLine == '' or speedLimitLine == ''):
                    return None
                else:
                    x = speedLine
                    y = speedLimitLine

                    self.lineCounter += 1

                    if x <= (y*constant):
                        self.countTrue += 1
                        return True
                    else:
                        self.countFalse += 1
                        return False, self.sound()

        speedInput.close()
        speedLimitInput.close()

        # Checking if driving always is OK. Just a method for test-file.
        if self.lineCounter == (self.countTrue + self.countFalse):
            if self.lineCounter != self.countTrue:
                return False
            else:
                return True


    def sound(self):
        return "Pip"

    # def checkIfTrue(self):
    #     # Checking if length match
    #     if self.lineCounter == (self.countTrue + self.countFalse):
    #         if self.lineCounter != self.countTrue:
    #             return False
    #         else:
    #             return True

# sp = SpeedLimit()
# print sp.openFile(speed, speedLimit)
