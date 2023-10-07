import cv2
import pyautogui as pg
import numpy as np
import user_input
# handle dispatch missions
def dispatching():
    screenshot = pg.screenshot()
    # adjust colors
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    # locate a single object in a screenshot
    board = pg.locateOnScreen(user_input.dispatch, confidence=.90)
    if board:
        pg.click(board.left+540, y=board.top+600)
        dispatching()