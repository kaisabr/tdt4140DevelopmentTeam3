# Skrevet av Magnus og Aashild


import unittest
from main_var3 import *


class MyTest(unittest.TestCase):

    def test1(self):
        self.assertTrue(distanceToCar().calculateOptimalDistance(10) > 0)
    def test2(self):
        self.assertEqual(distanceToCar().calculateOptimalDistance(30), 90)
    def test3(self):
        self.assertTrue(distanceToCar().siren(True, 20, 50))
    def test4(self):
        self.assertFalse(distanceToCar().siren(True, 20, 70))

if __name__ == '__main__':
    unittest.main()
