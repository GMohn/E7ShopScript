# Import necessary libraries
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

# Set pause and failsafe parameters for pyautogui
pg.PAUSE = .25
pg.FAILSAFE = True

# Define constants for prices and offsets
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

# Define the main function
def main():
    # Declare global variables
    global skystones,gold, num_mystic,num_book,bookFlag,mystFlag,huntFlag,bookmark,mystic,start,end
    
    # Get user input
    getUsr = input("enter ints sep by spaces (skystones gold bookmark mystics): ").split()

    # Check if the input is valid, if not, fill with zeros
    if len(getUsr) <= 3:
        for i in range(4):
            getUsr.append(0)
            if getUsr[i]:
                getUsr.pop(len(getUsr)-1)
            else:
                continue

    # If the first input is "hunt", start the hunt
    if getUsr[0] == "hunt":
        huntFlag = True
        start_hunt.startHunt()
        return

    # Assign the user inputs to the global variables
    skystones = int(getUsr[0]) or np.inf
    gold = int(getUsr[1]) or np.inf
    bookmark = int(getUsr[2]) or np.inf
    mystic = int(getUsr[3]) or np.inf 
    num_book = 0 
    num_mystic = 0
    bookFlag = False
    mystFlag = False

    # Initialize variables for the main loop
    spins = 0
    start, end = [],[]
    initialsky = skystones 
    initialgold = gold 
    initialbook = bookmark 
    initialmystic = mystic 

    # Main loop
    try:
        while(in_shop.inShop() and (not locate_objects.LocateObject(purchase)) and ((mystic > 0 and gold >= MYSTIC_PRICE) or (bookmark > 0 and gold >= BOOKMARK_PRICE))):
            bookFlag = False
            mystFlag = False
            start.append(time.time())
            dispatching()
            scrolled = False
            # Try to buy objects and if can decrement gold amount
            locate_objects.LocateObject(bookmarkico)
            locate_objects.LocateObject(mysticico)
            # Scroll and set flag to true
            scrolled = scroll.scroll()
            if not bookFlag:
                locate_objects.LocateObject(bookmarkico)
            if not mystFlag:
                locate_objects.LocateObject(mysticico)

            if scrolled:
                # Refresh shop
                if(skystones >= 3):
                    refreshing()
                else:
                    break        
            end.append(time.time())          
            spins += 1
            print("\rspins: ",spins," avg spin time: ",(sum(end)-sum(start))/(spins),"skystones used: ",str((spins)*3)+"/"+str(initialsky)," gold spent: ",str(num_book * BOOKMARK_PRICE+num_mystic * MYSTIC_PRICE)+"/"+str(initialgold),"bookmarks: ",str(num_book)+"/"+str(initialbook),"mystics: ",str(num_mystic)+"/"+str(initialmystic),end="\r")
    except KeyboardInterrupt:
        # Save file
        end.append(time.time())
        file_save.fileSave(spins)
        
    end.append(time.time())
    file_save.fileSave(spins)
