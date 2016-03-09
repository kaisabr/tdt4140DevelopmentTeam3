import unittest
import interiorLightAnalyzer

TL = interiorLightAnalyzer.interiorLightCheck()

lights = [1,1,1,1,0,0,0,0] #Test all possible combinations
door = [0,1,0,1,1,1,0,0]
f = 'farter.txt' #example file with different speeds
speed = TL.get_speeds(f) #useing the general method in the primary code to generate an array with only zeros and ones

class TestUM(unittest.TestCase):#give true if system should 'pip', if not, false

    def setUp(self):
        pass
    def test1(self):
        self.assertEqual(TL.interiorLightCheck(lights[0],door[0],speed[0]), False) #light on, door closed, 0 speed
    def test2(self):
        self.assertEqual(TL.interiorLightCheck(lights[1],door[1],speed[1]), True) #light on, door open, 0 speed
    def test3(self):
        self.assertEqual(TL.interiorLightCheck(lights[2],door[2],speed[2]), True) #light on, door closed, car with speed
    def test4(self):
        self.assertEqual(TL.interiorLightCheck(lights[3],door[3],speed[3]), True) #light on, door open, car with speed
    def test5(self): #lys av, dor aapen, bil stille
        self.assertEqual(TL.interiorLightCheck(lights[4],door[4],speed[4]), False) #light off, door open, 0 speed
    def test6(self):
        self.assertEqual(TL.interiorLightCheck(lights[5],door[5],speed[5]), False) #light off, door open, car with speed
    def test7(self):
        self.assertEqual(TL.interiorLightCheck(lights[6],door[6],speed[6]), False) #light off, door closed, car with speed
    def test8(self):
        self.assertEqual(TL.interiorLightCheck(lights[7],door[7],speed[7]), False) #light off, door closed, 0 speed


if __name__=='__main__':
    unittest.main()

