# External Librarys
import cv2 as cv
import pyautogui
import time

# Internal Librarys
from Modules.PhotoGrabber import PhotoGrabber


class PositionIdentifier:

    # Returns the location of the Bosses name plate
    def ReturnBossPosition():
        PhotoGrabber.GrabEnemysBars()
        greyEnemyBars = cv.cvtColor(cv.imread(cv.samples.findFile(
            "Bot2.0/Assets2.0/Comparisons/CompEnemyBar.jpg")),
            cv.COLOR_BGR2GRAY)
        greyBossName = cv.cvtColor(cv.imread(cv.samples.findFile(
            "Bot2.0\Assets2.0\Targets\Boss.JPG")),
            cv.COLOR_BGR2GRAY)

        positionBossName = cv.matchTemplate(
            greyEnemyBars, greyBossName, cv.TM_CCOEFF)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(positionBossName)

        pyautogui.moveTo(max_loc[0],  max_loc[1])

        print(max_loc)
        print("Threshold = {}".format(max_val))

        return max_loc

    # Returns the location of the Players name plate
    def ReturnPlayerPosition():
        PhotoGrabber.GrabPlayerBars()
        greyPlayerBars = cv.cvtColor(cv.imread(cv.samples.findFile(
            "Bot2.0/Assets2.0/Comparisons/CompPlayerBar.jpg")),
            cv.COLOR_BGR2GRAY)
        greyPlayerName = cv.cvtColor(cv.imread(cv.samples.findFile(
            "Bot2.0\Assets2.0\Targets\Player.JPG")),
            cv.COLOR_BGR2GRAY)

        positionPlayerName = cv.matchTemplate(
            greyPlayerBars, greyPlayerName, cv.TM_CCOEFF)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(positionPlayerName)

        pyautogui.moveTo(max_loc[0],  max_loc[1])

        print(max_loc)
        print("Threshold = {}".format(max_val))

        return max_loc

    def ReturnCurrentCard(inputTargetCard):
        PhotoGrabber.GrabPlayerBars()
        greyCurrentHand = cv.cvtColor(cv.imread(cv.samples.findFile(
            "Bot2.0/Assets2.0/Comparisons/CompPlayerBar.jpg")),
            cv.COLOR_BGR2GRAY)
        greyCard = cv.cvtColor(cv.imread(cv.samples.findFile(
            inputTargetCard)),
            cv.COLOR_BGR2GRAY)

        positionCurrentCard = cv.matchTemplate(
            greyCurrentHand, greyCard, cv.TM_CCOEFF)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(positionCurrentCard)

        pyautogui.moveTo(max_loc[0],  max_loc[1])

        print(max_loc)
        print("Threshold = {}".format(max_val))
        time.sleep(1)
        return max_loc
