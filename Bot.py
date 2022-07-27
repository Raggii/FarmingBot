import pyautogui
import time
from PIL import ImageGrab

import numpy as np
import cv2 as cv

import os
import sys

# state machine 4 states

# First is before battle
# Second is inside room
# Third is in battle
# Fouth is exit battle


class StateMachine():
    First = 0
    Second = 1
    Third = 2
    Forth = 3


""" Checks for the transition screen for wiz and if found returns True else 
False
"""


def CheckTransition():
    found = False
    realComp = cv.imread(cv.samples.findFile(
        "FarmingBot/Assets/Transition.jpg"))

    grabTransition()
    testComp = cv.imread(cv.samples.findFile(
        "FarmingBot/Assets/CompTrans.jpg"))

    while(not found):
        errorL2 = cv.norm(realComp, testComp, cv.NORM_L2)
        similarity = 1 - errorL2 / (150 * 140)
        print('Similarity = ', similarity)
        if(similarity > 0.7):
            print("FOUND!")
            found = True
        else:
            grabTransition()
            testComp = cv.imread(cv.samples.findFile(
                "FarmingBot/Assets/CompTrans.jpg"))


def itemDropped():

    found = False
    realComp = []
    realComp.append(
        cv.imread(cv.samples.findFile("FarmingBot/Assets/Drop0.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("FarmingBot/Assets/Drop1.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("FarmingBot/Assets/Drop2.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("FarmingBot/Assets/Drop3.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("FarmingBot/Assets/Drop4.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("FarmingBot/Assets/Drop5.jpg")))

    grabDrop()
    testComp = cv.imread(cv.samples.findFile("FarmingBot/Assets/CompDrop.jpg"))

    for comparison in realComp:
        errorL2 = cv.norm(comparison, testComp, cv.NORM_L2)
        similarity = 1 - errorL2 / (150 * 140)
        print('Similarity = ', similarity)
        if(similarity > 0.7):
            print("Battle END!")
            return True
    return False


def grabDrop():
    pic = ImageGrab.grab(bbox=(0, 960, 150, 1100))
    pic.save("FarmingBot/Assets/CompDrop.jpg")
    time.sleep(0.2)


def grabTransition():
    pic = ImageGrab.grab(bbox=(500, 500, 800, 800))
    pic.save("FarmingBot/Assets/CompTrans.jpg")
    time.sleep(0.2)


def grabExit():
    pic = ImageGrab.grab(bbox=(800, 200, 1000, 400))
    pic.save("FarmingBot/Assets/CompExit.jpg")
    time.sleep(0.2)


def Rotate90Degrees():
    pyautogui.moveTo(1200, 800)
    pyautogui.drag(80, 0, .6, button='right')

# Merge these when numbers are locked


""" Before Battle. have to move backwards and move mouse to click on team up
"""


def MoveOneStep(delay):
    pyautogui.mouseDown()
    pyautogui.mouseDown(button='right')
    time.sleep(delay)
    #currentState = StateMachine.Third
    pyautogui.mouseUp()
    pyautogui.mouseUp(button='right')
    time.sleep(delay)


def RotateAndMove(input):
    pyautogui.moveTo(1200, 800)
    pyautogui.drag(input, 0, .6, button='right')
    MoveOneStep(2.1)


def LeaveRoom():

    realComp = []
    realComp.append(
        cv.imread(cv.samples.findFile("FarmingBot/Assets/Exit1.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("FarmingBot/Assets/Exit2.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("FarmingBot/Assets/Exit3.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("FarmingBot/Assets/Exit4.jpg")))

    grabExit()
    testComp = cv.imread(cv.samples.findFile("FarmingBot/Assets/CompExit.jpg"))
    counter = 0
    for comparison in realComp:
        errorL2 = cv.norm(comparison, testComp, cv.NORM_L2)
        similarity = 1 - errorL2 / (150 * 140)
        print('Similarity = ', similarity)
        if(similarity > 0.7):
            if(counter == 0):
                RotateAndMove(113)
                return True
            elif(counter == 1):
                RotateAndMove(95)
                return True
            elif(counter == 2):
                RotateAndMove(70)
                return True
            elif(counter == 3):
                RotateAndMove(50)
                return True
        counter += 1
    return False


def TeamUp():
    xCoord = 1300
    yCoord = 1350
    pyautogui.moveTo(xCoord, yCoord)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(xCoord, yCoord - 300)
    pyautogui.click()


def FirstState(currentState):
    # move backwards 5 times

    Rotate90Degrees()
    MoveOneStep(0.2)
    time.sleep(0.3)
    TeamUp()
    CheckTransition()
    currentState = StateMachine.Second
    return currentState


""" In room. Move forward  for 15 steps """


def SecondState(currentState):
    # Move Forward 15 times

    MoveOneStep(2)
    currentState = StateMachine.Third
    return currentState


""" In Battle. Click in 1 spot to use attack card until circles come up on the 
side. Indicating that we have gotten items from the battle """


def ThirdState(currentState):

    if(itemDropped()):
        currentState = StateMachine.Forth
    else:
        xCoord = 1075
        yCoord = 730
        pyautogui.moveTo(xCoord, yCoord)
        pyautogui.click()

    return currentState


def ForthState(currentState):
    # grabDrop()
    found = False
    found = LeaveRoom()
    if(found):
        currentState = StateMachine.First
    return currentState


def main():
    currentState = StateMachine.Forth
    time.sleep(5)
    while(True):
        # check for if the F7 key is pressed when pressed start and stop the program
        # keyboard.is_pressed('f7')
        if(currentState == StateMachine.First):
            print("In First State")
            currentState = FirstState(currentState)
            # break
        elif(currentState == StateMachine.Second):
            print("In Second State")
            currentState = SecondState(currentState)
            # break
        elif(currentState == StateMachine.Third):
            print("In Third State")
            currentState = ThirdState(currentState)
            # break
        elif(currentState == StateMachine.Forth):
            print("In Forth State")
            currentState = ForthState(currentState)
            # break
        time.sleep(5)


main()
