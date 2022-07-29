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
        "Assets/Transition.jpg"))

    grabTransition()
    testComp = cv.imread(cv.samples.findFile(
        "Assets/CompTrans.jpg"))

    while(not found):
        errorL2 = cv.norm(realComp, testComp, cv.NORM_L2)
        similarity = 1 - errorL2 / (150 * 140)
        #print('Similarity = ', similarity)
        if(similarity > 0.7):
            print("FOUND!")
            found = True
        else:
            grabTransition()
            testComp = cv.imread(cv.samples.findFile(
                "Assets/CompTrans.jpg"))


def itemDropCircle():

    grabBook()
    book = cv.imread('Assets/CompBook.jpg', 0)
    bookReal = cv.imread('Assets/Book.jpg', 0)

    errorL2 = cv.norm(book, bookReal, cv.NORM_L2)
    similarity = 1 - errorL2 / (150 * 140)
    print('Similarity = ', similarity)
    if(similarity > 0.9):
        print("FOUND!")
        return True
    else:
        return False
    # if value error caught then we cant index into the list which means the list exists!


def grabDrop():
    pic = ImageGrab.grab(bbox=(0, 960, 150, 1100))
    pic.save("Assets/CompDrop.jpg")
    time.sleep(0.2)


def grabTransition():
    pic = ImageGrab.grab(bbox=(500, 500, 800, 800))
    pic.save("Assets/CompTrans.jpg")
    time.sleep(0.2)


def grabExit():
    pic = ImageGrab.grab(bbox=(800, 200, 1000, 400))
    pic.save("Assets/CompExit.jpg")
    time.sleep(0.2)


def grabBook():
    pic = ImageGrab.grab(bbox=(2400, 1250, 2475, 1400))
    pic.save("Assets/CompBook.jpg")
    time.sleep(0.2)


def Rotate90Degrees():
    pyautogui.moveTo(1200, 10)
    pyautogui.drag(80, 0, .6, button='right')


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


def Rotate(input):
    pyautogui.moveTo(1200, 800)
    pyautogui.drag(input, 0, .6, button='right')


def LeaveRoom():

    realComp = []
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit1.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit2.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit3.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit4.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit3Test.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit4Test.jpg")))

    grabExit()
    testComp = cv.imread(cv.samples.findFile("Assets/CompExit.jpg"))
    counter = 0
    for comparison in realComp:
        errorL2 = cv.norm(comparison, testComp, cv.NORM_L2)
        similarity = 1 - errorL2 / (150 * 140)
        #print('Similarity = ', similarity)
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
            elif(counter == 4):
                RotateAndMove(70)
                return True
            elif(counter == 5):
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


def getMana():
    MoveOneStep(0.5)
    Rotate(-22)
    MoveOneStep(5.8)
    Rotate(-8)
    MoveOneStep(0.9)
    time.sleep(5)
    Rotate(-11)
    MoveOneStep(1.5)
    time.sleep(20)
    Rotate(85)
    MoveOneStep(2)
    time.sleep(5)
    Rotate(35)
    MoveOneStep(1)
    Rotate(-15)
    MoveOneStep(4.5)
    Rotate(15)
    MoveOneStep(0.5)
    Rotate(100)


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
    #


""" In Battle. Click in 1 spot to use attack card until circles come up on the 
side. Indicating that we have gotten items from the battle """


def ThirdState(currentState):

    if(itemDropCircle()):
        currentState = StateMachine.Forth
    else:
        xCoord = 1075
        yCoord = 730
        pyautogui.moveTo(xCoord, yCoord)
        pyautogui.click()

    return currentState


def ForthState(currentState):
    # grabBook()
    found = False
    found = LeaveRoom()
    if(found):
        currentState = StateMachine.First
    return currentState


def main():
    counter = 1
    start = time.time()
    currentState = StateMachine.First
    time.sleep(5)
    while(True):
        # check for if the F7 key is pressed when pressed start and stop the program
        # keyboard.is_pressed('f7')
        if(currentState == StateMachine.First):
            print("In First State")
            if(counter % 60 == 0):
                getMana()
            currentState = FirstState(currentState)
            # break
        elif(currentState == StateMachine.Second):
            print("In Second State")
            currentState = SecondState(currentState)
            end = time.time()
            print(
                "\n\n\nTimes Killed = {}\nTime for Kill {:.2f} -------------------------\n\n\n".format(counter - 1, end - start))
            counter += 1
            start = time.time()

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
        endError = time.time()
        print(endError - start)
        if((endError - start) > 700):
            print("Code stalled -----------------------------------------")
            pic = ImageGrab.grab(bbox=(0, 0, 2500, 1500))
            pic.save("Assets/ERROR_REPORT.jpg")
            break


main()


# TODO
# Scroll out when starting
# add functionality to click boost damage cards to decrease time of battles.
# Remove unneeded Exits due to scrolling errors
# Add a Watch dog timer to stop the program if un responsive
#    - Make this give stats on last position to a Txt file so we can debug it
# Add functionallity into stage one that checks for health and mana
#    - If low then clicks poition or just runs outside and gets health and mana that way
# Change running times when exiting the level sometimes it will just run right outside of the battle
# also add a catch in state 4 that checks if the player has moved from the room yet
#    - add a transition checker and if not triggered then try movement again
# Add functionality to start the program using the F7 key while in game
#    - This could also be used to pause the program
# add stats for each of the states to get an idea of how long the bot is expected to be in each
# Have an automatically stat generating device that shows the above on a graph.
# Read from the chat to see if a specific drop has occoured?
