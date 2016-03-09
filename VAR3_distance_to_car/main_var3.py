# Skrevet av Magnus og Aashild

import siren

class distanceToCar():

	# Beregner optimal distanse.
	def calculateOptimalDistance(self,speed):
		return speed*3

	# Sirenen varsler dersom avstanden til bilen foran er for liten
	def siren(self,carIsOn, speed, distance):
		speed = carInput.getSpeed()
		distance = carInput.distanceToCarAhead()
		while carIsOn:
			if (self.calculateOptimalDistance(speed) < distance):
				siren.triggerByDistanceToCar()