import unittest
from itertools import izip
from VAR5speedreader import *


currentSpeedLimit = 80
speed_to_fast = 90
speed_OK = 60
speed = 60
speed_list_perfect = [30, 45, 69, 30, 72]
speed_list_to_fast = [30, 45, 60, 80, 100]

class MyTestCase(unittest.TestCase):

    # Testing if the code is giving you a message if you're driving to fast (over the speed limit)
    def testToFast(self):
        # self.assertTrue(SpeedLimit().drivingOK(speed_list_to_fast, currentSpeedLimit), False)
        self.assertTrue(SpeedLimit().drivingOK(speed_to_fast, currentSpeedLimit), False)

    # Testing if the code is giving you a message if you don't drive faster than the speed limit.
    def testPerfectSpeed(self):
        # self.assertTrue(SpeedLimit().drivingOK(speed_list_perfect, currentSpeedLimit), True)
        self.assertTrue(SpeedLimit().drivingOK(speed_OK, currentSpeedLimit), True)

    def test_DrivingToFast(self):
        self.assertFalse(SpeedLimit().drivingToFast(speed, currentSpeedLimit), "Driving to Fast")

    def test_OK(self):
        self.assertFalse(SpeedLimit().drivingToFast(speed, currentSpeedLimit))

    def test_DrivingToFast2(self):
         self.assertEquals(SpeedLimit().drivingToFast(speed_to_fast, currentSpeedLimit), True, "You are driving to fast")

    def test_OK2(self):
         self.assertEquals(SpeedLimit().drivingToFast(speed_OK, currentSpeedLimit), False, "You're driving is OK")


if __name__ == '__main__':
    unittest.main()
