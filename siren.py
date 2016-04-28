import winsound

class siren():

    def __init__(self):
        #The variables below determine whether the sound warning system for a given VAR is on or off.

        self.VAR1on = True
        self.VAR2on = True
        self.VAR3on = True
        self.VAR4on = True
        self.VAR5on = True


    #Method is used by VAR1
    def triggeredByVAR1(self):
        print "Check if your interior light is on"
        if self.VAR1on:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

    #Method is used by VAR2
    def triggeredByVAR2(self, text):
        print text
        if self.VAR2on:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


    #Method is used by VAR3
    def triggeredByVAR3(self):
        print "Distance to car in front is too small."
        if self.VAR3on:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


    #Method is used by VAR4
    def triggeredByVAR4(self):
        print "There is an object in your blind spot."
        if self.VAR4on:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


    #Method is used by VAR5
    def triggeredByVAR5(self):
        print "Driving too fast."
        if self.VAR5on:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

