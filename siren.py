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
        if self.VAR1on:
            print "Check if your interior light is on"

    #Method is used by VAR2
    def triggeredByVAR2(self, text):
        if self.VAR2on:
            print text

    #Method is used by VAR3
    def triggeredByVAR3(self):
        if self.VAR3on:
            print "Distance to car in front is too small."

    #Method is used by VAR4
    def triggeredByVAR4(self):
        if self.VAR4on:
            print "There is an object in your blind spot."

    #Method is used by VAR5
    def triggeredByVAR5(self):
        if self.VAR5on:
            print "There is an object in your blind spot."

