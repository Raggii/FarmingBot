# External Librarys
import time

# Internal Modules
from Modules.WizardMovement import WizardMovement


class FirstState:

    def LoadingBar():
        #This is important
        pass

    def InitalCountDown(self):

        # Maybe clear the terminal on restart?
        #import os
        # os.system('cls||clear')
        self.LoadingBar()
        print("Starting New and Advanced Bot!")
        # Add a cooler start up system with a cool loading bar!!
        time.sleep(3)

    def CompleteFirstState():
        WizardMovement.MoveOneStep(8)
        time.sleep(0.5)
        WizardMovement.EnterArea()
        time.sleep(1)
        WizardMovement.MoveOneStep(1)
        time.sleep(0.8)
        WizardMovement.EnterArea()
