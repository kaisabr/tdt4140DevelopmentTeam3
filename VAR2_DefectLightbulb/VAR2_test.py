import unittest
from lightbulbAnalyzer import *


lightSignalOff = 0 # Light is off
lightSignalOn = 1 # Light is on
carSignalOn = 1 # The car is turned on
brakeSignalOn = 1 # The brake is on
indicatorSwitchedOn = 1 # The indicator light is witched on

class MyTestCase(unittest.TestCase):

    def testIsLightOff(self):
        # check if you get a warning if front light is off
        self.assertEqual(lightBulbAnalyzer().isFrontLightOff(lightSignalOff, carSignalOn), "Front ligth is not on. Make sure it is working")

        # check if you get a warning if back light is off
        self.assertEqual(lightBulbAnalyzer().isBackLightOff(lightSignalOff, carSignalOn), "Back ligth is not on. Make sure it is working")

        # check if you get a warning if brake light is off
        self.assertEqual(lightBulbAnalyzer().isBrakeLightOn(carSignalOn, brakeSignalOn, lightSignalOff), "Brake light is not on. Make sure it is working")

        # check if you get a warning if licence plate light is off
        self.assertEqual(lightBulbAnalyzer().isLicencePlateLightOff(lightSignalOff, carSignalOn), "Licence plate ligth is not on. Make sure it is working")

        # check if you get a warning if indicator light is off
        self.assertEqual(lightBulbAnalyzer().isIndicatorLightOff(lightSignalOff, carSignalOn, indicatorSwitchedOn), "Please check your indicator light. No input to light sensor for 5 seconds")



if __name__ == '__main__':
    unittest.main()
