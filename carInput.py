import os
class carInput():

    def __init__(self):

        current_folder_path, current_folder_name = os.path.split(os.getcwd())

        file1 = open(current_folder_path+'\\speeds.txt', 'r') #speed file with different speeds
        textFromSpeedFile = file1.read()
        self.speeds = textFromSpeedFile.split('\n')

        file2 = open(current_folder_path+'\\interiorLight.txt','r') #status file for intertior ligjt (0s and 1s)
        textFromInteriorLightFile = file2.read()
        self.interiorLightStatus = textFromInteriorLightFile.split('\n')

        file3 =open(current_folder_path+'\\carDoors.txt','r') #1 if a door is open, 0 if not
        textFromDoorFile = file3.read()
        self.doorStatus = textFromDoorFile.split('\n')

        file4 =open(current_folder_path+'\\distanceToLeftSide.txt','r') #file with numbers for the distance to the left side of the car
        textFromLeftSideFile = file4.read()
        self.distanceToLeft = textFromLeftSideFile.split('\n')

        file5 =open(current_folder_path+'\\distanceToRightSide.txt','r') #file with numbers for the distance to the right side of the car
        textFromRightSideFile = file5.read()
        self.distanceToRight = textFromRightSideFile.split('\n')

        file6 =open(current_folder_path+'\\leftIndicatorLightIsOn.txt','r') #1 if left indicator light is on, 0 if not
        textFromLeftIndicatorFile = file6.read()
        self.leftIndicatorOn = textFromLeftIndicatorFile.split('\n')

        file7 =open(current_folder_path+'\\rightIndicatorLightIsOn.txt','r') #1 if right indicator light is on, 0 if not
        textFromRightIndicatorFile = file7.read()
        self.rightIndicatorOn = textFromRightIndicatorFile.split('\n')

        file8 =open(current_folder_path+'\\carIsOn.txt','r') #1 if car is on, 0 if not
        textFromCarIsOnFile = file8.read()
        self.carIsOn = textFromCarIsOnFile.split('\n')

    def getCurrentSpeed(self):
        while len(self.speeds) != 0:
            return self.speeds.pop(0)

    #Written by Andrea. Gives ut 0 if interior light is off, if on it gives 1
    #Used in: VAR1 (interiorLightAnalyzer)
    def isInteriorLightOn(self):
        while len(self.interiorLightStatus) != 0:
            light = self.interiorLightStatus.pop(0)
            return light

    def isDoorOpen(self):
        while len(self.doorStatus) != 0:
            door = self.doorStatus.pop(0)
            return door


    #Returns distance to object to the left side of the car. Method returns distance in meters. Used by VAR4. Written by Katharina and Magnus.
    def distanceToLeftSide(self):
        while len(self.distanceToLeft) != 0:
            return self.distanceToLeft.pop(0)

    #Returns distance to object to the right side of the car. Method returns distance in meters. Used by VAR4. Written by Katharina and Magnus.
    def distanceToRightSide(self):
        while len(self.distanceToRight) != 0:
            return self.distanceToRight.pop(0)

    #Returns whether left indicator light is on. Method returns answer in boolean. Used by VAR4. Written by Katharina and Magnus.
    def leftIndicatorLightIsOn(self):
        while len(self.leftIndicatorOn) != 0:
            res = self.leftIndicatorOn.pop(0)
            if res == 0:
                return False
            else:
                return True

    #Returns whether right indicator light is on. Method returns answer in boolean. Used by VAR4. Written by Katharina and Magnus.
    def rightIndicatorLightIsOn(self):
        while len(self.rightIndicatorOn) != 0:
            res = self.rightIndicatorOn.pop(0)
            if res == 0:
                return False
            else:
                return True

    def distanceToCar(self):
        pass

    def carIsOn(self):
        while len(self.carIsOn) != 0:
            res = self.carIsOn.pop(0)
            if res == 0:
                return False
            else:
                return True

    # Should check if switch for indicator light is activated
    def indicatorLightSwitchedOn(self, lightSignal):
        if lightSignal == 1:
            return True
        else:
            return False

    # Should check if brakes are used
    def brakePushed(self, brakeSignal):
        if brakeSignal == 1:
            return True
        else:
            return False

    # The method checks if the ligthsensor recieves input. Returns False if everything is OK.
    # sensorInput recieves either a 0, if the light is not on, and 1 if the light is on.
    def isLightOff(self, sensorInput):
        if sensorInput == 0:
            return True
        else:
            return False
