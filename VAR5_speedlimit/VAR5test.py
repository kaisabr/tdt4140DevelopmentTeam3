import unittest
from VAR5speedreader import *

#En fil med speedlimit
speedLimit = 'SpeedLimit.txt'
#en fil med current speed
speed = 'Speed.txt'


class MyTestCase(unittest.TestCase):


    # Testing if the code is giving you a message if you're driving to fast (over the speed limit)
    def testDriving(self):
        self.assertTrue(SpeedLimit().openFile(speed, speedLimit), False)

    # Testing if the code is giving you a message if you don't drive faster than the speed limit.
    def testOK(self):
        self.assertTrue(SpeedLimit().openFile(speed, speedLimit), True)


if __name__ == '__main__':
    unittest.main()
