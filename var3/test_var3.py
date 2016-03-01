# Skrevet av Magnus og Aashild


import unittest
import main_var3


MakeSiren = True


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(main_var3.getDistance() > 0)
    def test2(self):
        self.assertTrue(main_var3.getSpeed() > 0)
    def test3(self):
        self.assertTrue(main_var3.calculateOptimalDistance(main_var3.getSpeed()) > 0)
    def test4(self):
        self.assertEqual(main_var3.calculateOptimalDistance(30), 90)
    def test5(self):
        if main_var3.getDistance() < main_var3.calculateOptimalDistance(main_var3.getSpeed()):
            self.assertTrue(MakeSiren)


if __name__ == '__main__':
    unittest.main()
