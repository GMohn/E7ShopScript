# Import necessary libraries and modules
import user_input
import os.path

# Define the fileSave function
def fileSave(spins):
    # Print a message indicating that the program is saving data
    print("Saving...")
    # Define the name of the file to be written
    p = 'e7Stats.txt'
    # Initialize lists to store data
    fileList, totalList = [], []
    # Calculate the total gold spent on bookmarks and mystics
    goldOnBook = user_input.num_book * user_input.BOOKMARK_PRICE
    goldOnMyst = user_input.num_mystic * user_input.MYSTIC_PRICE
    totGold = goldOnBook + goldOnMyst
    # Calculate the total number of skystones used
    skystoneUsed = spins * 3
    # Define a list of strings to be used as labels for the data
    stringList = ["Bookmarks Bought: ","SkyStones per Bookmark: ", "Gold Spent on Bookmark: ","Mystics Bought:","Skystones per Mystic: ","Gold Spent on Mystic: ", "Number of Spins: ", "Skystones Used: ", "Gold Used: "]
    
    # Calculate the number of skystones spent per bookmark and mystic
    try:
        stonePerBook = spins*3/user_input.num_book
    except ZeroDivisionError:
        stonePerBook = 0

    try:
        stonePerMyst = spins*3/user_input.num_mystic
    except ZeroDivisionError:
        stonePerMyst = 0
    
    # Define a list of data to be written to the file
    seshList = [user_input.num_book, stonePerBook, goldOnBook, user_input.num_mystic, stonePerMyst, goldOnMyst, spins, skystoneUsed, totGold]

    # Check if the file exists
    if(os.path.exists(p) == False):
        # If the file does not exist, create it and write the data
        f = open(p, 'w+')
        for line in seshList:
            f.writelines(str(line)+"\n")
            totalList.append(str(line))
    else: 
        # If the file exists, open it in read and write mode
        f = open(p,'r+')
        # Read the existing data from the file
        lineList = f.readlines()
        # Calculate the total data by adding the new data and the existing data
        totalList = [float(seshList[i])+float(lineList[i]) for i in range (len(seshList))]
        # Calculate the average number of skystones spent per bookmark and mystic
        try:
            totalList[1] = totalList[7]/totalList[0]
        except ZeroDivisionError:
            pass

        try:
            totalList[4] = totalList[7]/totalList[3]
        except ZeroDivisionError:
            pass
        # Write the total data to the file
        f.seek(0)
        for line in totalList:
            f.writelines(str(line)+"\n")
    # Print the session stats and all-time stats
    print("\rSESH STATS\n----------\nSpins: ",spins,"\navg spin time: ",(sum(user_input.end)-sum(user_input.start))/(spins+1),"\nSkystones used: ",spins*3,"\nBookmarks: ",user_input.num_book,"\nMystics: ",user_input.num_mystic,"\nSkystones per Bookmark: ",stonePerBook,"\nSkystones per Mystic: ",stonePerMyst,"\nAmount of Gold used: ",totGold,"\n"*2,"ALL TIME STATS\n----------------")
    for i in range(len(totalList)):
        print(stringList[i]+str(totalList[i])+"\r")
    # Close the file
    f.close()
