# user_input.py
import pyautogui as pg
import numpy as np
import os.path
import time
import locate_objects
import scroll
from refresh import refreshing
import in_shop
import file_save
from dispatch import dispatching
import start_hunt

pg.PAUSE = .25
pg.FAILSAFE = True
BOOKMARK_PRICE = 184000
MYSTIC_PRICE = 280000
X_OFFSET = 750
Y_OFFSET = 70

# Get the path of the directory containing main.py
main_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(main_dir, 'assets')
# Get a list of all files in the assets folder
files = os.listdir(assets_dir)
# Iterate over the files
for file in files:
    # Get the file name without the extension
    file_name, _ = os.path.splitext(file)
    # Get the full path to the file
    file_path = os.path.join(assets_dir, file)
    # Create a global variable for the file path
    globals()[file_name] = file_path
def main():
    global skystones,gold, num_mystic,num_book,bookFlag,mystFlag,huntFlag,bookmark,mystic,start,end
    
    getUsr = input("enter ints sep by spaces (skystones gold bookmark mystics): ").split()
    if len(getUsr) <= 3:
        
        for i in range(4):
            getUsr.append(0)
            if getUsr[i]:
                getUsr.pop(len(getUsr)-1)
            else:
                continue
    if getUsr[0] == "hunt":
        huntFlag = True
        start_hunt.startHunt()
        return
    skystones = int(getUsr[0]) or np.inf
    gold = int(getUsr[1]) or np.inf
    bookmark = int(getUsr[2]) or np.inf
    mystic = int(getUsr[3]) or np.inf 
    num_book = 0 
    num_mystic = 0
    bookFlag = False
    mystFlag = False

    spins = 0
    start, end = [],[]
    initialsky = skystones 
    initialgold = gold 
    initialbook = bookmark 
    initialmystic = mystic 
    try:
        while(in_shop.inShop() and (not locate_objects.LocateObject(purchase)) and ((mystic > 0 and gold >= MYSTIC_PRICE) or (bookmark > 0 and gold >= BOOKMARK_PRICE))):
            bookFlag = False
            mystFlag = False
            start.append(time.time())
            dispatching()
            scrolled = False
            #try to buy objects and if can decrement gold amount
            locate_objects.LocateObject(bookmarkico)
            locate_objects.LocateObject(mysticico)
            #scroll and set flag to true
            scrolled = scroll.scroll()
            if not bookFlag:
                locate_objects.LocateObject(bookmarkico)
            if not mystFlag:
                locate_objects.LocateObject(mysticico)

            if scrolled:
                # refresh shop
                if(skystones >= 3):
                    refreshing()
                else:
                    break        
            end.append(time.time())          
            spins += 1
            print("\rspins: ",spins," avg spin time: ",(sum(end)-sum(start))/(spins),"skystones used: ",str((spins)*3)+"/"+str(initialsky)," gold spent: ",str(num_book * BOOKMARK_PRICE+num_mystic * MYSTIC_PRICE)+"/"+str(initialgold),"bookmarks: ",str(num_book)+"/"+str(initialbook),"mystics: ",str(num_mystic)+"/"+str(initialmystic),end="\r")
    except KeyboardInterrupt:
        end.append(time.time())
        file_save.fileSave(spins)
        #print("\n"*5)
    end.append(time.time())
    file_save.fileSave(spins)
