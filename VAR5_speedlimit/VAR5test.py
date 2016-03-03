import unittest
from VAR5speedreader import *

# File with speed limits
speedLimit = 'SpeedLimit.txt'

# file with speed (to fast)
speed = 'Speed.txt'

# file with speed OK
speedOK = 'SpeedOK.txt'



class MyTestCase(unittest.TestCase):


    # Testing if the code is giving you a message if you're driving to fast (over the speed limit)
    def testDriving(self):
        return self.assertTrue(SpeedLimit().openFile(speed, speedLimit), False)

    # Testing if the code is giving you a message if you don't drive faster than the speed limit.
    def testOK(self):
        return self.assertTrue(SpeedLimit().openFile(speedOK, speedLimit), True)


if __name__ == '__main__':
    print(unittest.main())
