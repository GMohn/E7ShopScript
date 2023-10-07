import pyautogui as pg

import user_input

def BuyObj(x,y):
    
    pg.click(x+user_input.X_OFFSET, y+user_input.Y_OFFSET)
    pg.press("r")
    pg.click(x+user_input.X_OFFSET, y+user_input.Y_OFFSET)
    pg.press("r")