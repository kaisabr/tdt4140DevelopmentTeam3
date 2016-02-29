# Skrevet av Magnus og Aashild


import unittest
import main_var3


MakeSiren = True


class MyTest(unittest.TestCase):
    def var3_test(self):
        self.assertTrue(main_var3.getDistance() > 0)
        self.assertTrue(main_var3.getSpeed() > 0)
        self.assertTrue(main_var3.calculateOptimalDistance(main_var3.getSpeed()) > 0)
        self.assertEqual(main_var3.calculateOptimalDistance(30), 90)
        if main_var3.getDistance() < main_var3.calculateOptimalDistance(main_var3.getSpeed()):
            self.assertTrue(MakeSiren)


if __name__ == '__main__':
    unittest.main()
