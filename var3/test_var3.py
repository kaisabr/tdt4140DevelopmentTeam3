import unittest

def main():


def getDistance():

def getSpeed():

def calculateOptimalDistance(speed):


def siren():


MakeSiren = True

distance = 0
speed = 0

class MyTest(unittest.TestCase):
    def var3_test(self):
        self.assertTrue(getDistance() > 0)
        self.assertTrue(getSpeed() > 0)
        self.assertTrue(calculateOptimalDistance(speed) > 0)
        self.assertEqual(calculateOptimalDistance(30), 90)
        if getDistance() < calculateOptimalDistance(speed):
            self.assertTrue(MakeSiren)


if __name__ == '__main__':
    unittest.main()

# time.sleep()