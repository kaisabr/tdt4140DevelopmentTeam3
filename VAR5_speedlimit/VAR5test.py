import unittest
import VAR5speedreader as sp
from VAR5speedreader import *


class MyTestCase(unittest.TestCase):

    # Testing if the code is giving you a message if you're driving to fast (over the speed limit)
    def testToFast(self, sp.speed, sp.currentSpeedLimit):
        for x in range(len(speed)):
            self.assertTrue(speed[x] < currentSpeedLimit*constant, "Driving to fast")

    #Testing if the code is giving you a message if you don't drive faster than the speed limit.
    def testPerfectSpeed(self, sp.speed, sp.currentSpeedLimit):
        for x in range(len(speed)):
            self.assertTrue(speed[x] > currentSpeedLimit*constant, "OK")



#test = MyTestCase()
#test.testToFast(SP.speed, SP.currentSpeedLimit)
#test.testPerfectSpeed(SP.speed, SP.currentSpeedLimit)


if __name__ == '__main__':
    unittest.main()
