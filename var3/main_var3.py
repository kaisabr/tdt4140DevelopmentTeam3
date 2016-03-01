# Skrevet av Magnus og Aashild

import random
import time



# Returnerer distanse til bilen foran
def getDistance():
	return random.randrange(5, 20)

# Returnerer fart i meter per sekund
def getSpeed():
	return random.randrange(0,30)

# Beregner optimal distanse
def calculateOptimalDistance(speed):
	return getSpeed()*3

# Sjekker om bilen er paa
def carIsOn():
	return True

# Sirenen varsler dersom avstanden til bilen foran er for liten
def siren():
	while carIsOn:
		time.sleep(1)
		if (calculateOptimalDistance(getSpeed()) > getDistance()):
			MakeSiren = True
			return MakeSiren
		else:
			MakeSiren = False
			return MakeSiren