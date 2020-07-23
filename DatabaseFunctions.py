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
        # fill getConfig list with data from the row in the spreadsheet
        for j in range(1, maxCol + 1):
            getCell = activeSched.cell(row = i, column = j)
            getConfig.append(getCell.value)
        # checking the values in getConfig
        print(*getConfig, sep = '\t')
        # query insert configuration into the db
        insertConfig = ('INSERT INTO Schedule VALUES (' + str(getConfig[0]) + ', \'' + getConfig[1] + '\', \'' + getConfig[2] + '\', ' + str(getConfig[3]) + ', ' + str(getConfig[4]) + ', ' + str(getConfig[5]) + ', ' + str(getConfig[6]) + ', ' + str(getConfig[7]) + ', ' + str(getConfig[8]) + ', \'' + getConfig[9] + '\');')
        # run query
        c = enigmaDB.cursor()
        c.execute(insertConfig)
        print('Config for day ' + str(getConfig[0]) + ' inserted into db.\n')
        c.close()
        enigmaDB.commit()

# get schedule from enigma database
def getSchedule(day):
    # get all row items in row matching day input by user
    getSched = 'SELECT * FROM Schedule WHERE Day = ' + str(day)
    c = enigmaDB.cursor()
    c.execute(getSched)
    schedResult = c.fetchone()
    c.close()
    # if schedResult is null, notify the user
    if not schedResult:
        print('No config found for Day ' + str(day))
    else:
        # return enigma configuration
        return schedResult

# close db connection
enigmaDB.close()

# create bombe db connection
bombeDB = sqlite3.connect('Bombe.db')

# insert message captured to database
def insertCapturedMsg():
    pass

# get CapturedMsg from bombe db
def getCapturedMsg():
    pass

# if found, add correct configuration to the known config table in the bombe db
def insertKnownConfig():
    pass

# delete wrong configuration from the bombe db
def wrongConfigFound():
    pass

# close db connection
bombeDB.close()

# Sources:
# help with xlsx file support found at https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/#:~:text=Openpyxl%20is%20a%20Python%20library,changes%20based%20on%20some%20criteria.