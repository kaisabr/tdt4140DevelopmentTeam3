import unittest
from lightbulbAnalyzer import *


lightSignalOff = 0 # Light is off
lightSignalOn = 1 # Light is on

class MyTestCase(unittest.TestCase):


    def testIsLightOff(self):
        self.assertEqual(lightBulbAnalyzer.isFrontLightOff(self, self.lightSignalOn), False)
        self.assertEquals(lightBulbAnalyzer.isBackLightOff(lightSignalOn), False)

    def testIsLightOn(self):



if __name__ == '__main__':
    unittest.main()
