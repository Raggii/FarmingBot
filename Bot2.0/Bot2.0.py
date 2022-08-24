# External Librarys
import time

# Internal Modules
from Modules.FirstState import FirstState
from Modules.MouseControl import MouseControl


def main():
    # FirstState.InitalCountDown(FirstState)
    # FirstState.CompleteFirstState()
    time.sleep(2)
    MouseControl.MoveToMultipleLocationsAndClick(
        MouseControl, [(0.5, 0.5), (0.5, 0.8), (2, 0.5), (0.5, 0.1), (0.2, 1), (-1, 0.5)])


main()
