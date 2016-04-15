import carInput
from VAR1 import interiorLightAnalyzer
from VAR2_DefectLightbulb import lightbulbAnalyzer
from VAR3_distance_to_car import distanceAnalyzer
from VAR4_blind_spot import blindSpotDetector
from VAR5_speedlimit import VAR5speedreader


class main():

        def __init__(self):
            self.car = carInput()
            self.var1 = interiorLightAnalyzer(self.car)
            self.var2 = lightbulbAnalyzer(self.car)
            self.var3 = distanceAnalyzer(self.car)
            self.var4 = blindSpotDetector(self.car)
            self.var5 = VAR5speedreader(self.car)

