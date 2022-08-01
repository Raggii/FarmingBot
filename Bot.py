from cv2 import LINE_8
import pyautogui
import time
from PIL import ImageGrab

import cv2 as cv


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
        "Assets/Comp/CompTrans.jpg"))

    errorL2 = cv.norm(realComp, testComp, cv.NORM_L2)
    similarity = 1 - errorL2 / (150 * 140)
    # If it finds transition then loops until its found
    if(similarity > 0.7):
        print("\n-------Transition Period Found ------- \n")
        while(not found):
            time.sleep(0.5)
            errorL2 = cv.norm(realComp, testComp, cv.NORM_L2)
            similarity = 1 - errorL2 / (150 * 140)
            if(similarity < 0.7):
                print("------- Transition Period Over -------\n")
                found = True
            else:
                grabTransition()
                testComp = cv.imread(cv.samples.findFile(
                    "Assets/Comp/CompTrans.jpg"))
    return found


def itemDropCircle():

    grabBook()
    book = cv.imread('Assets/Comp/CompBook.jpg', 0)
    bookReal = cv.imread('Assets/Book.jpg', 0)

    errorL2 = cv.norm(book, bookReal, cv.NORM_L2)
    similarity = 1 - errorL2 / (150 * 140)
    if(similarity > 0.9):
        print("Found Battle Exit Condition")
        return True
    else:
        return False
    # if value error caught then we cant index into the list which means the list exists!


def grabTransition():
    pic = ImageGrab.grab(bbox=(500, 500, 800, 800))
    pic.save("Assets/Comp/CompTrans.jpg")
    time.sleep(0.2)


def grabExit():
    pic = ImageGrab.grab(bbox=(800, 200, 1000, 400))
    pic.save("Assets/Comp/CompExit.jpg")
    time.sleep(0.2)


def grabBook():
    pic = ImageGrab.grab(bbox=(2400, 1250, 2475, 1400))
    pic.save("Assets/Comp/CompBook.jpg")
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
        cv.imread(cv.samples.findFile("Assets/Exit/Exit1.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit/Exit2.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit/Exit3.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit/Exit4.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit/Exit3Test.jpg")))
    realComp.append(
        cv.imread(cv.samples.findFile("Assets/Exit/Exit4Test.jpg")))

    grabExit()
    testComp = cv.imread(cv.samples.findFile("Assets/Comp/CompExit.jpg"))
    counter = 0
    for comparison in realComp:
        errorL2 = cv.norm(comparison, testComp, cv.NORM_L2)
        similarity = 1 - errorL2 / (200 * 200)
        if(similarity > 0.75):
            if(counter == 0):
                Rotate(113)
                print("Found Exit Number 1")
                return True
            elif(counter == 1):
                Rotate(95)
                print("Found Exit Number 2")
                return True
            elif(counter == 2):
                Rotate(70)
                print("Found Exit Number 3")
                return True
            elif(counter == 3):
                Rotate(50)
                print("Found Exit Number 4")
                return True
            elif(counter == 4):
                Rotate(70)
                print("Found Exit Number 3 Test")
                return True
            elif(counter == 5):
                Rotate(50)
                print("Found Exit Number 4 Test")
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
    print("------- OBTAINING MANA STAND BY -------")
    MoveOneStep(0.5)
    Rotate(-22)
    MoveOneStep(5.8)
    Rotate(-8)
    MoveOneStep(0.9)
    time.sleep(5)
    Rotate(-11)
    MoveOneStep(1.5)
    time.sleep(45)
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
    print("------- OBTAINING MANA COMPLETED -------\n")
    print("--------------- RESETTING --------------\n")


def grabCards():
    pic = ImageGrab.grab(bbox=(0, 0, 1780, 810))
    pic.save("Assets/Comp/CompCards.jpg")
    time.sleep(0.2)


def MoveToPower():

    grabCards()
    grayCards = cv.cvtColor(cv.imread(cv.samples.findFile(
        "Assets/Comp/CompCards.jpg")), cv.COLOR_BGR2GRAY)

    PowerUp = cv.imread(cv.samples.findFile("Assets/Battle/PowerUp.jpg"))
    grayPowerUp = cv.cvtColor(PowerUp, cv.COLOR_BGR2GRAY)
    resultPower = cv.matchTemplate(grayCards, grayPowerUp, cv.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(resultPower)
    pyautogui.moveTo(max_loc[0],  max_loc[1])
    time.sleep(1)
    pyautogui.click()

    pyautogui.moveTo(1000, 50)
    pyautogui.drag(50, 0, .6, button='right')


def MoveToDamage():

    grabCards()
    grayCards = cv.cvtColor(cv.imread(cv.samples.findFile(
        "Assets/Comp/CompCards.jpg")), cv.COLOR_BGR2GRAY)

    Damage = cv.imread(cv.samples.findFile("Assets/Battle/Damage.jpg"))

    GreyDamage = cv.cvtColor(Damage, cv.COLOR_BGR2GRAY)

    resultPower = cv.matchTemplate(grayCards, GreyDamage, cv.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(resultPower)

    pyautogui.moveTo(max_loc[0] + 20,  max_loc[1] + 20)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(1000, 50)
    pyautogui.drag(50, 0, .6, button='right')


def MoveToRealCard():
    grabCards()
    grayCards = cv.cvtColor(cv.imread(cv.samples.findFile(
        "Assets/Comp/CompCards.jpg")), cv.COLOR_BGR2GRAY)
    DamageReal = cv.imread(cv.samples.findFile("Assets/Battle/DamageReal.jpg"))

    GreyDamageReal = cv.cvtColor(DamageReal, cv.COLOR_BGR2GRAY)

    resultReal = cv.matchTemplate(grayCards, GreyDamageReal, cv.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(resultReal)

    pyautogui.moveTo(max_loc[0] + 20,  max_loc[1] + 20)
    time.sleep(1)
    pyautogui.click()


def SelectCards():

    MoveToPower()
    time.sleep(0.5)
    MoveToDamage()
    time.sleep(0.5)
    MoveToRealCard()


def grabOddCard():
    pic = ImageGrab.grab(bbox=(1300, 660, 1380, 780))
    pic.save("Assets/Comp/CompOddCard.jpg")
    time.sleep(0.2)


def grabEvenCard():
    pic = ImageGrab.grab(bbox=(1250, 660, 1330, 780))
    pic.save("Assets/Comp/CompEvenCard.jpg")
    time.sleep(0.2)


def cardsExist():

    grabOddCard()
    testOdd = cv.imread(cv.samples.findFile("Assets/Comp/CompOddCard.jpg"))

    realOdd = []
    realOdd.append(
        cv.imread(cv.samples.findFile("Assets/Battle/OddDamage.jpg")))
    realOdd.append(
        cv.imread(cv.samples.findFile("Assets/Battle/OddPowerUp.jpg")))

    for comparison in realOdd:
        errorL2 = cv.norm(comparison, testOdd, cv.NORM_L2)
        similarity = 1 - errorL2 / (200 * 200)
        if(similarity > 0.85):
            print("Found Odd Card Set")
            return True

    grabEvenCard()
    testEven = cv.imread(cv.samples.findFile("Assets/Comp/CompEvenCard.jpg"))

    realEven = []
    realEven.append(
        cv.imread(cv.samples.findFile("Assets/Battle/EvenDamage.jpg")))
    realEven.append(
        cv.imread(cv.samples.findFile("Assets/Battle/EvenPowerUp.jpg")))

    for comparison in realEven:
        errorL2 = cv.norm(comparison, testEven, cv.NORM_L2)
        similarity = 1 - errorL2 / (200 * 200)
        if(similarity > 0.85):
            print("Found Odd Card Set")
            return True

    return False


def FirstState(currentState):
    # move backwards 5 times
    found = False
    Rotate90Degrees()
    MoveOneStep(0.2)
    time.sleep(0.8)
    TeamUp()
    while(not found):
        found = CheckTransition()
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

    if(itemDropCircle()):
        currentState = StateMachine.Forth
    else:
        if(cardsExist()):

            SelectCards()

    return currentState


def ForthState(currentState):
    # grabBook()
    found = False
    foundTrans = False
    # Finds room location and rotates to exit of room
    found = LeaveRoom()

    if(found):
        while(not foundTrans):
            MoveOneStep(0.75)
            foundTrans = CheckTransition()
            time.sleep(0.25)
        currentState = StateMachine.First
    return currentState


def CountDown():
    print("Application Starting, Countdown 5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("--------- Successful Lauch ---------")


def main():
    counter = 1
    start = time.time()
    currentState = StateMachine.First
    CountDown()
    while(True):
        # check for if the F7 key is pressed when pressed start and stop the program
        # keyboard.is_pressed('f7')
        if(currentState == StateMachine.First):
            print("In First State")
            if(counter % 25 == 0):
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
        time.sleep(3.5)
        endError = time.time()
        print("Time Since Last Kill = {:.2f}".format(endError - start))
        if((endError - start) > 700):
            print("Code stalled -----------------------------------------")
            pic = ImageGrab.grab(bbox=(0, 0, 2500, 1500))
            pic.save("Assets/ERROR_REPORT.jpg")
            break


main()


# TODO
# Scroll out when starting
# Add functionality to start the program using the F7 key while in game
#    - This could also be used to pause the program
# Put all assests into specific files for easy to navigate code
