import carInput
from VAR1 import interiorLightAnalyzer
from VAR2_DefectLightbulb import lightbulbAnalyzer
from VAR3_distance_to_car import distanceAnalyzer
from VAR4_blind_spot import blindSpotDetector
from VAR5_speedlimit import VAR5speedreader
from siren import *
from threading import Thread

class main():

        def __init__(self):
            self.car = carInput()
            self.siren = siren()

            self.var1object = interiorLightAnalyzer(self.car, self.siren)
            self.var2object = lightbulbAnalyzer(self.car, self.siren)
            self.var3object = distanceAnalyzer(self.car, self.siren)
            self.var4object = blindSpotDetector(self.car, self.siren)
            self.var5object = VAR5speedreader(self.car, self.siren)

            self.VAR1loop = runVAR1(self.var1object)
            self.VAR2loop = runVAR2(self.var2object)
            self.VAR3loop = runVAR3(self.var3object)
            self.VAR4loop = runVAR4(self.var4object)
            self.VAR5loop = runVAR5(self.var5object)


            #Her skal det stå funksjonalitet som gjør det mulig å slå av varslingssystemet, og slå av lydvarsler for èn eller flere funksjoner.


class runVAR1(Thread):

    def __init__(self, var1):
        super(runVAR1, self).__init__()
        self.daemon = True
        self.start()

    def run(self):
        #Aktiverer VAR hvert n-te sekund.



class runVAR2(Thread):

    def __init__(self, var2):
        super(runVAR2, self).__init__()
        self.daemon = True
        self.start()

    def run(self):
        #Aktiverer VAR hvert n-te sekund.



class runVAR3(Thread):

    def __init__(self, var3):
        super(runVAR3, self).__init__()
        self.daemon = True
        self.start()

    def run(self):
        #Aktiverer VAR hvert n-te sekund.



class runVAR4(Thread):

    def __init__(self, var4):
        super(runVAR4, self).__init__()
        self.daemon = True
        self.start()


    def run(self):
        #Aktiverer VAR hvert n-te sekund.



class runVAR5(Thread):

    def __init__(self, var5):
        super(runVAR5, self).__init__()
        self.daemon = True
        self.start()


    def run(self):
        #Aktiverer VAR hvert n-te sekund.

