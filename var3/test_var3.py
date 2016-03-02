# Skrevet av Magnus og Aashild


import unittest
import main_var3


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(main_var3.calculateOptimalDistance(10) > 0)
    def test2(self):
        self.assertEqual(main_var3.calculateOptimalDistance(30), 90)
    def test3(self):
        self.assertTrue(main_var3.siren(True, 20, 50))
    def test4(self):
        self.assertFalse(main_var3.siren(True, 20, 70))

if __name__ == '__main__':
    unittest.main()
