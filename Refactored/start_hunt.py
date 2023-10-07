import time
import locate_objects
import pyautogui as pg
import user_input
def startHunt():
    pg.click(700,100)
    #pg.press("w")
    while True:
        if locate_objects.LocateObject(user_input.hunt) or locate_objects.LocateObject(user_input.nrg20):
            pg.press("w")
        if locate_objects.LocateObject(user_input.nrg):
            pg.press("r")
        time.sleep(10)