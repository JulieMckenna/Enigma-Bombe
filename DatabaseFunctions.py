# functions for the enigma/bombe machines to interface with their respective databases
# author: Chandler Berry

import sqlite3, openpyxl

# create enigma db connection
enigmaDB = sqlite3.connect('Enigma.db')

# file path of test file (Chandler) --- 'G:\\gitrepos\\Enigma-Bombe\\enigma.xlsx'
# add enigma schedule to db
def createEnigmaSchedule(filePath):
    # open xlsx file and get the number of rows, each row indicates an enigma configuration for a particular day
    sched = openpyxl.load_workbook(filePath)
    activeSched = sched.active
    maxRow = activeSched.max_row
    maxCol = activeSched.max_column
    getConfig = []
    
    # get the configuration for each day 
    for i in range(1, maxRow + 1):
        for j in range(1, maxCol + 1):
            getCell = activeSched.cell(row = i, column = j)
            getConfig.append(getCell.value)
        print(*getConfig, sep = '\t')
        # insert configuration into the db
        insConfig = ('INSERT INTO Schedule VALUES (' + getConfig[0] + ', \'' + getConfig[1] + '\', \'' ');') # FINISH WRITING THIS OUT
        c = enigmaDB.cursor()
        c.execute(insConfig)
        c.close()
        # enigmaDB.commit()
    

# close db connection
enigmaDB.close()

# create bombe db connection
bombeDB = sqlite3.connect('Bombe.db')

# insert message captured to database
def insCapturedMsg():
    pass

# get CapturedMsg from bombe db
def getCapturedMsg():
    pass

# if found, add correct configuration to the known config table in the bombe db
def insKnownConfig():
    pass

# delete wrong configuration from the bombe db
def wrongConfigFound():
    pass

# close db connection
bombeDB.close()

# testing createEnigmaSchedule
createEnigmaSchedule('G:\\gitrepos\\Enigma-Bombe\\enigma.xlsx')

# help with xlsx file support found at https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/#:~:text=Openpyxl%20is%20a%20Python%20library,changes%20based%20on%20some%20criteria.