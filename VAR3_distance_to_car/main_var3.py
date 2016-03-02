# Skrevet av Magnus og Aashild

import random

# Returnerer distanse til bilen foran. Foreloepig redundant metode.
def getDistance():
	return random.randrange(5, 20)

# Returnerer fart i meter per sekund. Foreloepig redundant metode.
def getSpeed():
	return random.randrange(0,30)

# Beregner optimal distanse.
def calculateOptimalDistance(speed):
	return speed*3

# Sjekker om bilen er paa. Foreloepig redundant metode.
def carIsOn():
	return True

# Sirenen varsler dersom avstanden til bilen foran er for liten
def siren(carIsOn, speed, distance):
	while carIsOn:
		if (calculateOptimalDistance(speed) > distance):
			MakeSiren = True
			return MakeSiren
		else:
			MakeSiren = False
			return MakeSiren