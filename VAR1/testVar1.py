import unittest
from lysITaketKode import taklys
lys = [1,1,1,1,0,0,0,0]
dor = [0,1,0,1,1,1,0,0]
fart = [0,0,1,1,0,1,1,0]

lys2 = [10110001]
dor2 = [01011101]
fart2 = [00110110]


class TestUM(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):
        self.assertEqual(taklys(lys[0],dor[0],fart[0]), False)
    def test2(self):
        self.assertEqual(taklys(lys[1],dor[1],fart[1]), True)
    def test3(self):
        self.assertEqual(taklys(lys[2],dor[2],fart[2]), True)
    def test4(self):
        self.assertEqual(taklys(lys[3],dor[3],fart[3]), True)
    def test5(self):
        self.assertEqual(taklys(lys[4],dor[4],fart[4]), False) 
    def test6(self):
        self.assertEqual(taklys(lys[5],dor[5],fart[5]), False)
    def test7(self):
        self.assertEqual(taklys(lys[6],dor[6],fart[6]), False)
    def test8(self):
        self.assertEqual(taklys(lys[7],dor[7],fart[7]), False)


if __name__=='__main__':
    unittest.main()

