# ARNA, MAREN AND MATHILDE

import unittest
from VAR5speedreader import *

# File with speed limits
speedLimit = 'SpeedLimit.txt'

# file with speed OK
speed = 'Speed.txt'

# file with speed (to fast)
speedToFast = 'SpeedToFast.txt'


class MyTestCase(unittest.TestCase):

    # Testing if the code is giving you a message if you're driving to fast (over the speed limit)
    def testDriving(self):
        self.assertEqual(SpeedLimit().openFile(speedToFast, speedLimit), False)

    # Testing if the code is giving you a message if you don't drive faster than the speed limit.
    def testOK(self):
        self.assertEqual(SpeedLimit().openFile(speed, speedLimit), True)


if __name__ == '__main__':
    unittest.main()
