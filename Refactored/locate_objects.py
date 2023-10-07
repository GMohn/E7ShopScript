import pyautogui as pg
import time
import buy_objects
import user_input

# Define the LocateObject function
def LocateObject(object):
    # Take a screenshot to locate objects on
    time.sleep(.25)
    screenshot = pg.screenshot()

    # Locate a single object in a screenshot
    board = pg.locateOnScreen(object, confidence=.95)

    # If the object is found
    if board:
        # If the object is the bookmark icon and there are bookmarks available
        if (object == user_input.bookmarkico and user_input.bookmark > 0):
            # Buy the object
            buy_objects.BuyObj(board.left, board.top)
            # Update gold, bookmark, and book count
            user_input.gold -= user_input.BOOKMARK_PRICE
            user_input.bookmark -= 1
            user_input.num_book += 1
            # Set bookFlag to True
            user_input.bookFlag = True
        # If the object is the mystic icon and there are mystics available
        elif (object == user_input.mysticico and user_input.mystic > 0):
            # Buy the object
            buy_objects.BuyObj(board.left, board.top)
            # Update gold, mystic, and mystic count
            user_input.gold -= user_input.MYSTIC_PRICE
            user_input.mystic -= 1
            user_input.num_mystic += 1
            # Set mystFlag to True
            user_input.mystFlag = True
        # If the object is the hunt or nrg20 icon
        elif (object == user_input.hunt or object == user_input.nrg20):
            # Click on the object
            pg.click(board.left,board.top)
            # Press "w"
            pg.press("w")
        # Return True if the object is found
        return True
    # Return False if the object is not found
    return False
