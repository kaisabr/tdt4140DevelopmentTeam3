#metoden returnerer false dersom alt er OK (ingen notification til kjorer) ellers true
class interiorLight:


    def taklys(self,l, d, f): #tar inn en verdi for om lys er paa/av, dor aapen/lukket, bil fart/stille, alle verdier 0 eller 1
        if l == 1 and d == 0 and f == 0: #eneste gangen det er ok at lyset faktisk er paa
            return False
        elif l==1: #om den gaar hit, vil enten dor vaere aapen og/eller bil ha fart
            return True
        else:
            return False #lyset er av, skal ikke varsle

