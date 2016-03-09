# Skrevet av Magnus og Aashild

import random

class distanceToCar():

	# Beregner optimal distanse.
	def calculateOptimalDistance(self,speed):
		return speed*3

	# Sirenen varsler dersom avstanden til bilen foran er for liten
	def siren(self,carIsOn, speed, distance):
		while carIsOn:
			if (self.calculateOptimalDistance(speed) > distance):
				MakeSiren = True
				return MakeSiren
			else:
				MakeSiren = False
				return MakeSiren