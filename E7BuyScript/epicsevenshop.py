#################################
#
#  Script to locate objects on
#         a screenshot
#
#               by
#
#        Geoffrey Mohn
#
#################################
# R is buy D is confirm refresh position is space
# packages
import cv2
import numpy as np
import pyautogui as pg

# take a screenshot to store locally
#screenshot = pg.screenshot('screenshot.png')
x_offset = 750
y_offset = 50
# take a screenshot to locate objects on
screenshot = pg.screenshot()

# adjust colors
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
def findObject(object):
    
    # locate a single object in a screenshot
    board = pg.locateOnScreen(object, confidence=.90)
    
    # draw rectangle around the object
    if board:
        # click buy button 
        pg.click(x=board.left+x_offset, y=board.top+y_offset)
        cv2.rectangle(
            screenshot,
            (board.left+750, board.top+30),
            (board.left + board.width+750, board.top + board.height+30),
            (150, 255, 255),
            2
        )
        cv2.rectangle(
            screenshot,
            (board.left, board.top),
            (board.left + board.width, board.top + board.height),
            (0, 255, 255),
            2
        )
        return True, board
    return False , board
# detect several objects on screenshot
'''for pawn in pg.locateAllOnScreen('pawn.png', confidence=0.5):
    # draw rectangle around the object
    cv2.rectangle(
        screenshot,
        (pawn.left, pawn.top),
        (pawn.left + pawn.width, pawn.top + pawn.height),
        (0, 0, 255),
        2
    )'''
findObject("bookmark.PNG")
bookmarkInfo = findObject("mysticbuy.png")
if bookmarkInfo[0]:
    findObject("bookmarkbuy.png")
    
# display screenshot in a window
cv2.imshow('Screenshot', screenshot)

# escape condition
cv2.waitKey(0)

# clean up windows
cv2.destroyAllWindows()