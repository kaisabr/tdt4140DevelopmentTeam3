#class for interior light

class interiorLightAnalyzer:
    #Method returns the speeds in 0s and 1s

        
    #the method returns flase if everything is OK (no notifications), if not, it returns false
    def interiorLightCheck(self,l, d, s): #take in value for light, door and speed (1 or 0)
    #siren =  Siren.siren(boolean), i følge UML-diagrammet har sirene-klassen en boolsk sirene-metode
        if l == 1 and d == 0 and s == 0: #the only time it is ok for the light to be on
            return False
            #siren = Siren.siren(False)
        elif l==1: #light is on, but dor is open or/and the car has a speed
            return True
            #siren = Siren.siren(True)
        else:
            return False #the light is off, no notification necessary
            #siren = Siren.siren(False)
            
    

