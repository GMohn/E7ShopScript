import user_input
import os.path
# function to write to a txt file of overall stats
#  bookmarks SSperbook goldonbook mystics SSpermyst goldonmyst spins skystones totgold
def fileSave(spins):
    print("Saving...")
    p = 'e7Stats.txt'
    fileList,totalList = [],[]
    goldOnBook = user_input.num_book * user_input.BOOKMARK_PRICE
    goldOnMyst = user_input.num_mystic * user_input.MYSTIC_PRICE
    totGold = goldOnBook+goldOnMyst
    skystoneUsed = spins * 3
    stringList = ["Bookmarks Bought: ","SkyStones per Bookmark: ", "Gold Spent on Bookmark: ","Mystics Bought:","Skystones per Mystic: ","Gold Spent on Mystic: ", "Number of Spins: ", "Skystones Used: ", "Gold Used: "]
    
    try:
        stonePerBook = spins*3/user_input.num_book
        
    except ZeroDivisionError:
        stonePerBook = 0

    try:
        stonePerMyst = spins*3/user_input.num_mystic
        
    except ZeroDivisionError:
        stonePerMyst = 0

    seshList = [user_input.num_book,stonePerBook,goldOnBook,user_input.num_mystic,stonePerMyst,goldOnMyst,spins,skystoneUsed,totGold]

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
        
    print("\rSESH STATS\n----------\nSpins: ",spins,"\navg spin time: ",(sum(user_input.end)-sum(user_input.start))/(spins+1),"\nSkystones used: ",spins*3,"\nBookmarks: ",user_input.num_book,"\nMystics: ",user_input.num_mystic,"\nSkystones per Bookmark: ",stonePerBook,"\nSkystones per Mystic: ",stonePerMyst,"\nAmount of Gold used: ",totGold,"\n"*2,"ALL TIME STATS\n----------------")
    for i in range(len(totalList)):
        print(stringList[i]+str(totalList[i])+"\r")
    f.close()
