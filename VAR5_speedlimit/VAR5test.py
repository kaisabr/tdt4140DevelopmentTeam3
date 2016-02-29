import unittest
import VAR5speedreader as sp
from VAR5speedreader import *


# speed = [30, 45, 69, 30, 72]

currentSpeedLimit = 80
speed = 66

class MyTestCase(unittest.TestCase):

    # # Testing if the code is giving you a message if you're driving to fast (over the speed limit)
    # def testToFast(self):
    #     for x in range(len(speed)-1):
    #         self.assertTrue(speed[x] < currentSpeedLimit*constant, "Driving to fast")
    #
    # #Testing if the code is giving you a message if you don't drive faster than the speed limit.
    # def testPerfectSpeed(self):
    #     for x in range(len(speed)-1):
    #         self.assertTrue(speed[x] > currentSpeedLimit*constant, "OK")

    #def testSpeed(self):
    #     self.assertTrue(sp.speedLimit.drivingToFast(speed, currentSpeedLimit), "Driving to fast")

    def testSpeed(self):
        self.assertEquals(self, sp.speedLimit.drivingToFast2(self.speed, self.currentSpeedLimit), "OK")



if __name__ == '__main__':
    unittest.main()
