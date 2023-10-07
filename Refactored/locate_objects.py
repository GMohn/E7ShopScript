import pyautogui as pg
import time
import buy_objects
import user_input
def LocateObject(object):
    # take a screenshot to locate objects on
    time.sleep(.25)
    screenshot = pg.screenshot()
    # adjust colors
    #screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # locate a single object in a screenshot
    board = pg.locateOnScreen(object, confidence=.95)
    # click to buy
    if board:
        if (object == user_input.bookmarkico and user_input.bookmark > 0):
            buy_objects.BuyObj(board.left, board.top)
            user_input.gold -= user_input.BOOKMARK_PRICE
            user_input.bookmark -= 1
            user_input.num_book += 1
            user_input.bookFlag = True
        elif (object == user_input.mysticico and user_input.mystic > 0):
            buy_objects.BuyObj(board.left, board.top)
            user_input.gold -= user_input.MYSTIC_PRICE
            user_input.mystic -= 1
            user_input.num_mystic += 1
            user_input.mystFlag = True
        elif (object == user_input.hunt or object == user_input.nrg20):
            pg.click(board.left,board.top)
            pg.press("w")
        return True # debug to just locate objects for now
    return False