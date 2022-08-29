# External Librarys
from PIL import ImageGrab
import time

# Internal Librarys


class PhotoGrabber:

    def TakeImagePercentage():
        pass

    def GrabEnemysBars():
        pic = ImageGrab.grab(bbox=(0, 0, 2200, 200))
        pic.save("Bot2.0/Assets2.0/Comparisons/CompEnemyBar.jpg")
        time.sleep(0.2)

    def GrabPlayerBars():
        pic = ImageGrab.grab(bbox=(0, 0, 2300, 1400))
        pic.save("Bot2.0/Assets2.0/Comparisons/CompPlayerBar.jpg")
        time.sleep(0.2)

    def GrabCurrentCards():
        pic = ImageGrab.grab(bbox=(0, 0, 1780, 810))
        pic.save("Bot2.0/Assets2.0/Comparisons/CompCards.jpg")
        time.sleep(0.2)

    def GrabBattleExit():
        pic = ImageGrab.grab(bbox=(2400, 1250, 2475, 1400))
        pic.save("Bot2.0/Assets2.0/Comparisons/CompBook.jpg")
        time.sleep(0.2)

    def grabTransition():
        pic = ImageGrab.grab(bbox=(500, 500, 800, 800))
        pic.save("Bot2.0/Assets2.0/Comparisons/CompTrans.jpg")
        time.sleep(0.2)
