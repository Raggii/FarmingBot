# External Librarys
import time

# Internal Modules
from Modules.FirstState import FirstState
from Modules.MouseControl import MouseControl

from Modules.PositionIdentifier import PositionIdentifier


def main():
    time.sleep(2)

    # PositionIdentifier.ReturnBossPosition()
    # PositionIdentifier.ReturnPlayerPosition()
    listOfCards = ["Bot2.0/Assets2.0/Targets/Card0.jpg",
                   "Bot2.0/Assets2.0/Targets/Card1.jpg",
                   #    "Bot2.0/Assets2.0/Targets/Card2.jpg",
                   #    "Bot2.0/Assets2.0/Targets/Card3.jpg",
                   #    "Bot2.0/Assets2.0/Targets/Card4.jpg",
                   #    "Bot2.0/Assets2.0/Targets/Card5.jpg"
                   ]

    for card in listOfCards:
        PositionIdentifier.ReturnCurrentCard(card)


main()
