# ARNA, MAREN AND MATHILDE

import unittest
from VAR5speedreader import *

# File with speed limits
speedLimit = 'SpeedLimit.txt'

# file with speed OK
speed = 'Speed.txt'

# file with speed (to fast)
speedToFast = 'SpeedToFast.txt'


# Maa ha noe til car og siren, for at vi ikke skal faa feilmelding, altsaa noen attributter

class MyTestCase(unittest.TestCase):

    # Testing if the code is giving you a message if you're driving to fast (over the speed limit)
    def testDriving(self):
        self.assertEqual(SpeedLimit(car, siren).checkSpeed(speedToFast, speedLimit), False)

    # Testing if the code is giving you a message if you don't drive faster than the speed limit.
    def testOK(self):
        self.assertEqual(SpeedLimit(car, siren).checkSpeed(speed, speedLimit), True)


if __name__ == '__main__':
    unittest.main()
