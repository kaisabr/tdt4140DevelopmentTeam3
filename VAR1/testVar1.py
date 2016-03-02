import unittest
import lysITaketKode

TL = lysITaketKode.interiorLight()

lys = [1,1,1,1,0,0,0,0] #Tester alle mulige kombinasjoner
dor = [0,1,0,1,1,1,0,0]
fart1 = open('farter.txt','r') #aapner fil med hastigheter til bilen
fart=[] #oppretter tom liste for aa legge inn 0 eller 1 ettersom bilen staar stille eller ikke

for line in fart1: #legger inn 1 naar bilen har fart, og 0 naar bilen star stille

    if line.strip() != str(0):
        fart.append(1) #bil har fart
    else:
        fart.append(0) #bil har ikke fart

class TestUM(unittest.TestCase):#gir ut true dersom den skal pipe, false om den ikke skal pipe

    def setUp(self):
        pass
    def test1(self):
        self.assertEqual(TL.taklys(lys[0],dor[0],fart[0]), False) #lys paa, dor lukket, bil stille
    def test2(self):
        self.assertEqual(TL.taklys(lys[1],dor[1],fart[1]), True) #lys paa, dor aapen, bil stille
    def test3(self):
        self.assertEqual(TL.taklys(lys[2],dor[2],fart[2]), True) #lys paa, dor lukket, bil fart
    def test4(self):
        self.assertEqual(TL.taklys(lys[3],dor[3],fart[3]), True) #lys paa, dor aapen, bil fart
    def test5(self): #lys av, dor aapen, bil stille
        self.assertEqual(TL.taklys(lys[4],dor[4],fart[4]), False) #lys av, dor aapen, bil stille
    def test6(self):
        self.assertEqual(TL.taklys(lys[5],dor[5],fart[5]), False) #lys av, dor aapen, bil fart
    def test7(self):
        self.assertEqual(TL.taklys([6],dor[6],fart[6]), False) #lys av, dor lukket, bil fart
    def test8(self):
        self.assertEqual(TL.taklys(lys[7],dor[7],fart[7]), False) #lys av, dor lukket, bil stille


if __name__=='__main__':
    unittest.main()

