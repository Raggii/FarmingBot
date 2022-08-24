# External Librarys
import pyautogui
import time


class WizardMovement:

    # Moves the player forward for half a second
    def MoveOneStep(delay):
        # One second is to long for average movement so to clean up inputs
        # divide by two.
        delay = delay/2
        pyautogui.mouseDown()
        pyautogui.mouseDown(button='right')
        time.sleep(delay)
        pyautogui.mouseUp()
        pyautogui.mouseUp(button='right')

    # Rotates the player by the inputted degrees
    def Rotate(degrees):
        # Does some funky math to get an approximate spin amount
        # Not exact but gives a reasonable approximation
        scaled_degrees = degrees/4.1
        pyautogui.moveTo(1200, 800)
        pyautogui.drag(scaled_degrees, 0, 1, button='right')

    def EnterArea():
        pyautogui.keyDown('x')
        time.sleep(0.1)
        pyautogui.keyUp('x')
