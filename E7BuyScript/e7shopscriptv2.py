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
# R is buy D is confirm refresh space is refresh down is scroll
# packages
import cv2
import numpy as np
import pyautogui as pg
import os.path
import time
pg.PAUSE = .25
pg.FAILSAFE = True
BOOKMARK_PRICE = 184000
MYSTIC_PRICE = 280000
X_OFFSET = 750
Y_OFFSET = 70


def LocateObject(object):
    global gold, bookmark, mystic,num_book,num_mystic,bookFlag,mystFlag
    # take a screenshot to locate objects on
    time.sleep(.25)
    screenshot = pg.screenshot()

    # adjust colors
    #screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # locate a single object in a screenshot
    board = pg.locateOnScreen(os.path.abspath(object), confidence=.90)
    # click to buy
    if board:
        if (object == "bookmark.png" and bookmark > 0):
            BuyObj(board.left, board.top)
            gold -= BOOKMARK_PRICE
            bookmark -= 1
            num_book += 1
            bookFlag = True
        elif (object == "mystic.png" and mystic > 0):
            BuyObj(board.left, board.top)
            gold -= MYSTIC_PRICE
            mystic -= 1
            num_mystic += 1
            mystFlag = True
        elif (object == "hunt.png" or object == "20nrg.png"):
            pg.click(board.left,board.top)
            pg.press("w")
        return True # debug to just locate objects for now
    return False
def startHunt():
    pg.click(700,100)
    #pg.press("w")
    while True:
        if LocateObject("hunt.png") or LocateObject("20nrg.png"):
            pg.press("w")
        if LocateObject("nrg.png"):
            pg.press("r")
        time.sleep(10)


def BuyObj(x,y):
    
    pg.click(x+X_OFFSET, y+Y_OFFSET)
    pg.press("r")
    pg.press("r")

def scroll():
    pg.press("down")
    return True

def refresh():
    global skystones
    pg.press(" ")
    
     #These are to be put in when we optimize the sleep time
    pg.press("d")

    pg.press("d")
    skystones -= 3
    
def  inShop():
       # take a screenshot to locate objects on
    screenshot = pg.screenshot()

    # adjust colors
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # locate a single object in a screenshot
    board = pg.locateOnScreen(os.path.abspath("shop.png"), confidence=.90)
    if board:
        pg.click(board.left+X_OFFSET, y=board.top)
        
        return True
    # change back to false after finding out why it cant find the his face
    return False

# function to write to a txt file of overall stats
#  bookmarks SSperbook goldonbook mystics SSpermyst goldonmyst spins skystones totgold
def fileSave(spins):
    print("Saving...")
    global num_mystic,num_book,start,end
    p = 'e7Stats.txt'
    fileList,totalList = [],[]
    goldOnBook = num_book * BOOKMARK_PRICE
    goldOnMyst = num_mystic * MYSTIC_PRICE
    totGold = goldOnBook+goldOnMyst
    skystoneUsed = spins * 3
    stringList = ["Bookmarks Bought: ","SkyStones per Bookmark: ", "Gold Spent on Bookmark: ","Mystics Bought:","Skystones per Mystic: ","Gold Spent on Mystic: ", "Number of Spins: ", "Skystones Used: ", "Gold Used: "]
    
    try:
        stonePerBook = spins*3/num_book
        
    except ZeroDivisionError:
        stonePerBook = 0

    try:
        stonePerMyst = spins*3/num_mystic
        
    except ZeroDivisionError:
        stonePerMyst = 0

    seshList = [num_book,stonePerBook,goldOnBook,num_mystic,stonePerMyst,goldOnMyst,spins,skystoneUsed,totGold]

    if(os.path.exists(p) == False):
        f = open(p, 'w+')
        for line in seshList:
            f.writelines(str(line)+"\n")
            totalList.append(str(line))
    
    else: 
        f = open(p,'r+')
        lineList = f.readlines()
        totalList = [float(seshList[i])+float(lineList[i]) for i in range (len(seshList))]
        try:
            totalList[1] = totalList[7]/totalList[0]
        
        except ZeroDivisionError:
            pass

        try:
            totalList[4] = totalList[7]/totalList[3]
        
        except ZeroDivisionError:
            pass
        # temp fix to fix total number of spins 
        #totalList[6] = totalList[7]/3
        
        f.seek(0)
        for line in totalList:
            f.writelines(str(line)+"\n")
        
    print("\rSESH STATS\n----------\nSpins: ",spins,"\navg spin time: ",(sum(end)-sum(start))/(spins+1),"\nSkystones used: ",spins*3,"\nBookmarks: ",num_book,"\nMystics: ",num_mystic,"\nSkystones per Bookmark: ",stonePerBook,"\nSkystones per Mystic: ",stonePerMyst,"\nAmount of Gold used: ",totGold,"\n"*2,"ALL TIME STATS\n----------------")
    for i in range(len(totalList)):
        print(stringList[i]+str(totalList[i])+"\r")
    f.close()

# handle dispatch missions
def dispatch():
    screenshot = pg.screenshot()
    # adjust colors
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    # locate a single object in a screenshot
    board = pg.locateOnScreen(os.path.abspath("dispatch.png"), confidence=.90)
    if board:
        pg.click(board.left+540, y=board.top+600)
        dispatch()

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
        startHunt()
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
        while(inShop() and (not LocateObject("purchase.png")) and ((mystic > 0 and gold >= MYSTIC_PRICE) or (bookmark > 0 and gold >= BOOKMARK_PRICE))):
            bookFlag = False
            mystFlag = False
            start.append(time.time())
            dispatch()
            scrolled = False
            #try to buy objects and if can decrement gold amount
            LocateObject("bookmark.png")
            LocateObject("mystic.png")
            #scroll and set flag to true
            scrolled = scroll()
            if not bookFlag:
                LocateObject("bookmark.png")
            if not mystFlag:
                LocateObject("mystic.png")

            if scrolled:
                # refresh shop
                if(skystones >= 3):
                    refresh()
                else:
                    break        
            end.append(time.time())          
            spins += 1
            print("\rspins: ",spins," avg spin time: ",(sum(end)-sum(start))/(spins),"skystones used: ",str((spins)*3)+"/"+str(initialsky)," gold spent: ",str(num_book * BOOKMARK_PRICE+num_mystic * MYSTIC_PRICE)+"/"+str(initialgold),"bookmarks: ",str(num_book)+"/"+str(initialbook),"mystics: ",str(num_mystic)+"/"+str(initialmystic),end="\r")
    except KeyboardInterrupt:
        end.append(time.time())
        fileSave(spins)
        #print("\n"*5)
    end.append(time.time())
    fileSave(spins)


main()