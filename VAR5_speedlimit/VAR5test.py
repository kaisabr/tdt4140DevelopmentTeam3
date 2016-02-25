import unittest
from VAR5speedreader import *

constant = 1.1

class MyTestCase(unittest.TestCase):

    # Testing if the code is giving you a message if you're driving to fast (over the speed limit)
    def testToFast(self, speed, speedlimit):
        self.assertTrue(speed*constant < speedlimit, "Driving to fast")

    #Testing if the code is giving you a message if you don't drive faster than the speed limit.
    def testPerfectSpeed(self, speed, speedlimit):
        self.assertTrue(speed*constant > speedlimit, "OK")



if __name__ == '__main__':
    unittest.main()
