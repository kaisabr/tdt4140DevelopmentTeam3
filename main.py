from carInput import carInput
import time
from VAR1.interiorLightAnalyzer import interiorLightAnalyzer
from VAR2_DefectLightbulb.lightbulbAnalyzer import lightBulbAnalyzer
from VAR3_distance_to_car.distanceAnalyzer import distanceAnalyzer
from VAR4_blind_spot.blindSpotDetector import blindSpotDetector
from VAR5_speedlimit.VAR5speedreader import SpeedLimit

from siren import siren
from threading import Thread

class main():

        def __init__(self):
            self.car = carInput()
            self.siren = siren()

            # This is a boolean variable that determines whether the program is turned on or off.
            self.on = True

            # These are boolean variables that determine whether a VAR is turned on or off.
            self.VAR1on = True
            self.VAR2on = True
            self.VAR3on = True
            self.VAR4on = True
            self.VAR5on = True

            print 'Enter a number to toggle warnings for corresponding VAR.\nEnter a letter a-e to toggle on/off for corresponding VAR.\nEnter 6 to toggle on/off for entire program.\n\n'

            self.var1object = interiorLightAnalyzer(self.car, self.siren)
            self.var2object = lightBulbAnalyzer(self.car, self.siren)
            self.var3object = distanceAnalyzer(self.car, self.siren)
            self.var4object = blindSpotDetector(self.car, self.siren)
            self.var5object = SpeedLimit(self.car, self.siren)

            self.VAR1loop = runVAR1(self.var1object, self)
            self.VAR2loop = runVAR2(self.var2object, self)
            self.VAR3loop = runVAR3(self.var3object, self)
            self.VAR4loop = runVAR4(self.var4object, self)
            self.VAR5loop = runVAR5(self.var5object, self)

            numberlist = ['1', '2', '3', '4', '5']
            letterlist = ['a', 'b', 'c', 'd', 'e']
            loopContinues = True

            while loopContinues:
                input = raw_input()

                if input in numberlist:
                    self.toggleWarning(input)
                if input in letterlist:
                    self.toggleOnOff(input)
                if input == '6':
                    self.on = not self.on

            #When this loop exits, the program shuts down.

        #By changing the values of the booleans on the siren-object, the warning systems for the given function is toggled on and off.
        def toggleWarning(self, i):
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

        def toggleOnOff(self, i):
            if i == 'a':
                self.VAR1on = not self.VAR1on
            if i == 'b':
                self.VAR2on = not self.VAR2on
            if i == 'c':
                self.VAR3on = not self.VAR3on
            if i == 'd':
                self.VAR4on = not self.VAR4on
            if i == 'e':
                self.VAR5on = not self.VAR5on



class runVAR1(Thread):

    def __init__(self, var1, mainobject):
        super(runVAR1, self).__init__()
        self.daemon = True
        self.var1 = var1
        self.mainobject = mainobject
        self.start()

    def run(self):
        while True:
            if self.mainobject.VAR1on and self.mainobject.on:
                self.var1.interiorLightCheck()
                time.sleep(5)


class runVAR2(Thread):

    def __init__(self, var2, mainobject):
        super(runVAR2, self).__init__()
        self.daemon = True
        self.var2 = var2
        self.mainobject = mainobject
        self.start()

    def run(self):
        while True:
            if self.mainobject.VAR2on and self.mainobject.on:
                self.var2.isFrontLightOff()
                self.var2.isBackLightOff()
                self.var2.isLicencePlateLightOff()
                self.var2.isIndicatorLightOff()
                self.var2.isBrakeLightOn()
                time.sleep(10)


class runVAR3(Thread):

    def __init__(self, var3, mainobject):
        super(runVAR3, self).__init__()
        self.daemon = True
        self.var3 = var3
        self.mainobject = mainobject
        self.start()

    def run(self):
        while True:
            if self.mainobject.VAR3on and self.mainobject.on:
                self.var3.calculateIfTooCloseToCar()
                time.sleep(7)


class runVAR4(Thread):

    def __init__(self, var4, mainobject):
        super(runVAR4, self).__init__()
        self.daemon = True
        self.var4 = var4
        self.mainobject = mainobject
        self.start()

    def run(self):
        while True:
            if self.mainobject.VAR4on and self.mainobject.on:
                self.var4.main()
                time.sleep(3)


class runVAR5(Thread):

    def __init__(self, var5, mainobject):
        super(runVAR5, self).__init__()
        self.daemon = True
        self.var5 = var5
        self.mainobject = mainobject
        self.start()


    def run(self):
        while True:
            if self.mainobject.VAR5on and self.mainobject.on:
                self.var5.checkSpeed()
                time.sleep(13)

