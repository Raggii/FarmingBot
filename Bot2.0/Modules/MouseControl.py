# External Librarys
import pyautogui
import time

# Internal Librarys

xCoordinate = 0
yCoordinate = 1


class MouseControl:

    # returns a tuple of the screens resolution
    def GetScreenResolution():
        return pyautogui.size()

    def MoveToLocationPercent(self, inputTuple):

        (xCoord, yXoord) = self.GetScreenResolution()
        if(inputTuple[xCoordinate] == 1):
            xCoord = xCoord - 1
        if(inputTuple[yCoordinate] == 1):
            yXoord = yXoord - 1
        scaledScreenSize = (
            xCoord * inputTuple[xCoordinate], yXoord * inputTuple[yCoordinate])

        # If the location is not on the screen does not complete action
        if(not pyautogui.onScreen(scaledScreenSize[xCoordinate], scaledScreenSize[yCoordinate])):
            return False
        else:
            pyautogui.moveTo(
                scaledScreenSize[xCoordinate], scaledScreenSize[yCoordinate])
            return True

    def MoveToLocationAndClick(self, inputTuple):
        returnValue = self.MoveToLocationPercent(self, inputTuple)
        pyautogui.click()
        return returnValue

    def MoveToMultipleLocationsAndClick(self, inputArrayTuples):
        counter = 0
        for inputTuple in inputArrayTuples:
            errorChecker = self.MoveToLocationAndClick(self, inputTuple)
            time.sleep(0.5)
            if(not errorChecker):
                print("Tuple {} contains an out of bounds error".format(counter))
            counter += 1
