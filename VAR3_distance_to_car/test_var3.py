# Skrevet av Magnus og Aashild


import unittest
from main_var3 import *


class MyTest(unittest.TestCase):

    def test1(self):
        self.assertTrue(distanceToCar().calculateOptimalDistance() > 0)
    def test2(self):
       # if(self.car.distanceToCar() = 40): Slik kan man visst ikke skrive
            self.assertEqual(distanceToCar().calculateOptimalDistance(), 120)
    def test3(self):
        # Mangel
        self.assertTrue(distanceToCar().calculateIfToCloseToCar())
    def test4(self):
       # if (self.car.getCurrentSpeed = 2):
            self.assertFalse(distanceToCar().calculateIfToCloseToCar())

if __name__ == '__main__':
    unittest.main()
