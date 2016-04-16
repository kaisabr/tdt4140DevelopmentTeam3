from carInput import carInput
import time
from VAR1.interiorLightAnalyzer import interiorLightAnalyzer
from VAR2_DefectLightbulb.lightbulbAnalyzer import lightBulbAnalyzer
from VAR3_distance_to_car.distanceAnalyzer import distanceAnalyzer
from VAR4_blind_spot.blindSpotDetector import blindSpotDetector
from VAR5_speedlimit.VAR5speedreader import SpeedLimit

from siren import siren
from threading import Thread

VAR1on = True
VAR2on = True
VAR3on = True
VAR4on = True
VAR5on = False

class main():

        def __init__(self):
            self.car = carInput()
            self.siren = siren()

            self.var1object = interiorLightAnalyzer(self.car, self.siren)
            self.var2object = lightBulbAnalyzer(self.car, self.siren)
            self.var3object = distanceAnalyzer(self.car, self.siren)
            self.var4object = blindSpotDetector(self.car, self.siren)
            self.var5object = SpeedLimit(self.car, self.siren)

            self.var2object.isFrontLightOff()

            self.VAR1loop = runVAR1(self.var1object)
            self.VAR2loop = runVAR2(self.var2object)
            self.VAR3loop = runVAR3(self.var3object)
            self.VAR4loop = runVAR4(self.var4object)
            self.VAR5loop = runVAR5(self.var5object)

            numberlist = ['1', '2', '3', '4', '5']
            loopContinues = True

            while loopContinues:
                input = raw_input('Enter a number to toggle warnings for corresponding VAR. Enter 6 to exit.')
                if input in numberlist:
                    self.toggle(input)
                if input == '6':
                    loopContinues = False

            #When this loop exits, the program shuts down.

        #By changing the values of the booleans on the siren-object, the warning systems for the given function is toggled on and off.
        def toggle(self, i):
            i = int(i)
            if i == 1:
                self.siren.VAR1on = not self.siren.VAR1on
            if i == 2:
                self.siren.VAR2on = not self.siren.VAR2on
            if i == 3:
                self.siren.VAR3on = not self.siren.VAR3on
            if i == 4:
                self.siren.VAR4on = not self.siren.VAR4on
            if i == 5:
                self.siren.VAR5on = not self.siren.VAR5on


class runVAR1(Thread):

    def __init__(self, var1):
        super(runVAR1, self).__init__()
        self.daemon = True
        self.var1 = var1
        self.start()

    def run(self):
        while VAR1on:
            self.var1.interiorLightCheck()
            time.sleep(5)



class runVAR2(Thread):

    def __init__(self, var2):
        super(runVAR2, self).__init__()
        self.daemon = True
        self.var2 = var2
        self.start()

    def run(self):
        while VAR2on:
            self.var2.isFrontLightOff()
            self.var2.isBackLightOff()
            self.var2.isLicencePlateLightOff()
            self.var2.isIndicatorLightOff()
            self.var2.isBrakeLightOn()
            time.sleep(10)



class runVAR3(Thread):

    def __init__(self, var3):
        super(runVAR3, self).__init__()
        self.daemon = True
        self.var3 = var3
        self.start()


    def run(self):
        while VAR3on:
            self.var3.calculateIfTooCloseToCar()
            time.sleep(0.5)



class runVAR4(Thread):

    def __init__(self, var4):
        super(runVAR4, self).__init__()
        self.daemon = True
        self.var4 = var4
        self.start()


    def run(self):
        while VAR4on:
            self.var4.main()
            time.sleep(0.5)



class runVAR5(Thread):

    def __init__(self, var5):
        super(runVAR5, self).__init__()
        self.daemon = True
        self.var5 = var5
        self.start()


    def run(self):
        while VAR5on:
            self.var5.checkSpeed()
            time.sleep(1)

