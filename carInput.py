import os
import sys
class carInput():

    def __init__(self):

        current_folder_path, current_folder_name = os.path.split(os.getcwd())
        sys.path.append(current_folder_path + "\*")

        file1 = open(current_folder_path+'\\'+current_folder_name+'\\speeds.txt', 'r') #speed file with different speeds   Mathilde tok vekk: '+current_folder_name+'\\
        textFromSpeedFile = file1.read()
        self.speeds = textFromSpeedFile.split('\n')

        file2 = open(current_folder_path+'\\'+current_folder_name+'\\interiorLight.txt','r') #status file for intertior ligjt (0s and 1s)
        textFromInteriorLightFile = file2.read()
        self.interiorLightStatus = textFromInteriorLightFile.split('\n')

        file3 =open(current_folder_path+'\\'+current_folder_name+'\\carDoors.txt','r') #1 if a door is open, 0 if not
        textFromDoorFile = file3.read()
        self.doorStatus = textFromDoorFile.split('\n')

        file4 =open(current_folder_path+'\\'+current_folder_name+'\\distanceToLeftSide.txt','r') #file with numbers for the distance to the left side of the car
        textFromLeftSideFile = file4.read()
        self.distanceToLeft = textFromLeftSideFile.split('\n')

        file5 =open(current_folder_path+'\\'+current_folder_name+'\\distanceToRightSide.txt','r') #file with numbers for the distance to the right side of the car
        textFromRightSideFile = file5.read()
        self.distanceToRight = textFromRightSideFile.split('\n')

        file6 =open(current_folder_path+'\\'+current_folder_name+'\\leftIndicatorLightIsOn.txt','r') #1 if left indicator light is on, 0 if not
        textFromLeftIndicatorFile = file6.read()
        self.leftIndicatorOn = textFromLeftIndicatorFile.split('\n')

        file7 =open(current_folder_path+'\\'+current_folder_name+'\\rightIndicatorLightIsOn.txt','r') #1 if right indicator light is on, 0 if not
        textFromRightIndicatorFile = file7.read()
        self.rightIndicatorOn = textFromRightIndicatorFile.split('\n')

        file8 =open(current_folder_path+'\\'+current_folder_name+'\\carIsOn.txt','r') #1 if car is on, 0 if not
        textFromCarIsOnFile = file8.read()
        self.carIsOnVariable = textFromCarIsOnFile.split('\n')

        file9 =open(current_folder_path+'\\'+current_folder_name+'\\indicatorLightSwitchedOn.txt','r') #1 if indicator light switch is on, 0 if not
        textIndicatorLightSwitchedOnFile = file9.read()
        self.indicatorLightSwitchedOnVariable = textIndicatorLightSwitchedOnFile.split('\n')

        file10 =open(current_folder_path+'\\'+current_folder_name+'\\brakePushed.txt','r') #1 if car is brake is pushed, 0 if not
        textFromBrakePushedFile = file10.read()
        self.brakePushedVariable = textFromBrakePushedFile.split('\n')

        file11 =open(current_folder_path+'\\'+current_folder_name+'\\isLightOff.txt','r') #1 if car is light is on, 0 if not. Arna and Maren should clarify what type of light this method actually checks.
        textFromIsLightOffFile = file11.read()
        self.isLightOffVariable = textFromIsLightOffFile.split('\n')

        file12 =open(current_folder_path+'\\'+current_folder_name+'\\distanceToCarFront.txt','r') # File contains numbers representing distance to car in front. Measured in meters.
        textFromDistanceToCarFront = file12.read()
        self.distanceToCarFrontVariable = textFromDistanceToCarFront.split('\n')

        file13 =open(current_folder_path+'\\'+current_folder_name+'\\speedLimits.txt','r') # File contains numbers representing speed limits. Speeds are measured in km/h.
        textFromSpeedLimits = file13.read()
        self.speedLimitsVariable = textFromSpeedLimits.split('\n')

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
        while len(self.distanceToCarFrontVariable) != 0:
            return self.distanceToCarFrontVariable.pop(0)

    def carIsOn(self):
        while len(self.carIsOnVariable) != 0:
            res = self.carIsOnVariable.pop(0)
            if res == 0:
                return False
            else:
                return True

    # Should check if switch for indicator light is activated
    def indicatorLightSwitchedOn(self):
        while len(self.indicatorLightSwitchedOnVariable) != 0:
            res = self.indicatorLightSwitchedOnVariable.pop(0)
            if res == 0:
                return False
            else:
                return True

    # Should check if brakes are used
    def brakePushed(self):
        while len(self.brakePushedVariable) != 0:
            res = self.brakePushedVariable.pop(0)
            if res == 0:
                return False
            else:
                return True

    # The method checks if the ligthsensor recieves input. Returns False if everything is OK.
    # sensorInput recieves either a 0, if the light is not on, and 1 if the light is on.
    def isLightOff(self):
        while len(self.isLightOffVariable) != 0:
            res = self.isLightOffVariable.pop(0)
            if res == 0:
                return False
            else:
                return True

    def getSpeedLimit(self):
        while len(self.speedLimitsVariable) != 0:
            return self.speedLimitsVariable.pop(0)
