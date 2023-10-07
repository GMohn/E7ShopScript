import cv2
import pyautogui as pg
import os.path
import user_input
import numpy as np

def  inShop():
       # take a screenshot to locate objects on
    screenshot = pg.screenshot()

    # adjust colors
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # locate a single object in a screenshot
    board = pg.locateOnScreen(os.path.abspath(user_input.shop), confidence=.90)
    if board:
        pg.click(board.left+user_input.X_OFFSET, y=board.top)
        
        return True
    # change back to false after finding out why it cant find the his face
    return False