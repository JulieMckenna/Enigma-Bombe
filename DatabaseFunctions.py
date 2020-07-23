# functions for the enigma/bombe machines to interface with their respective databases
# author: Chandler Berry

import sqlite3, openpyxl

# create enigma db connection
enigmaDB = sqlite3.connect('EnigmaDatabase.db')

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
        e = enigmaDB.cursor()
        e.execute(insertConfig)
        print('Config for day ' + str(getConfig[0]) + ' inserted into db.\n')
        e.close()
        enigmaDB.commit()

# createEnigmaSchedule('G:\\gitrepos\\Enigma-Bombe\\enigma.xlsx')

# get schedule from enigma database when function is provided with a day
def getConfiguration(day):
    # get all row items in row matching day input by user
    getSched = 'SELECT * FROM Schedule WHERE Day = ' + str(day)
    e = enigmaDB.cursor()
    e.execute(getSched)
    schedResult = e.fetchone()
    e.close()
    # if schedResult is null, notify the user
    if not schedResult:
        print('No config found for Day ' + str(day))
    else:
        # save plugboard setting 
        plugString = schedResult[1][0] + schedResult[2][0] + ',' + schedResult[1][1] + schedResult[2][1] + ',' + schedResult[1][2] + schedResult[2][2] + ',' + schedResult[1][3] + schedResult[2][3] + ',' + schedResult[1][4] + schedResult[2][4] + ',' + schedResult[1][5] + schedResult[2][5] + ',' + schedResult[1][6] + schedResult[2][6] + ',' + schedResult[1][7] + schedResult[2][7] + ',' + schedResult[1][8] + schedResult[2][8] + ',' + schedResult[1][9] + schedResult[2][9]
        # save list of settings in a usable format for the rest of enigma
        configuration = (schedResult[0], plugString, schedResult[3], schedResult[4], schedResult[5], schedResult[6], schedResult[7], schedResult[8], schedResult[9])
        # return enigma configuration
        return configuration

# close db connection
enigmaDB.close()

# create bombe db connection
bombeDB = sqlite3.connect('BombeDatabase.db')

# insert message captured into database
def insertCapturedMsg(msg, day):
    try:
        # logic to create new message ID
        getMsgID = 'SELECT MAX(MessageID) FROM CapturedMsg'
        b = bombeDB.cursor()
        b.execute(getMsgID)
        msgID = b.fetchone()
        b.close()
        newID = None
        if msgID[0] == None:
            newID = 1
        else:
            newID = msgID[0] + 1
        # insert new captured message into the database
        insertMessage = 'INSERT INTO CapturedMsg VALUES (' + str(newID) + ', \'' + msg + '\', 0, NULL, ' + str(day) + ');'
        b = bombeDB.cursor()
        b.execute(insertMessage)
        b.close()
        bombeDB.commit()
        print('Message saved.')
    except sqlite3.OperationalError:
        print('\nError when trying to insert values, please check the database connection and/or values being input.\n')
    except sqlite3.IntegrityError:
        print('\nError when trying to insert values, this configuration already exists in the database.\n')

# get CapturedMsg from bombe db
def getCapturedMsg(msgID):
    # find message in database with matching message id
    getMessage = 'SELECT * FROM CapturedMsg WHERE MessageID = ' + str(msgID)
    b = bombeDB.cursor()
    b.execute(getMessage)
    msgData = b.fetchone()
    b.close()
    # if message is not found, print that to the user
    if msgData == None:
        returnMsg = 'No message in database with that ID.'
        return returnMsg
    else:
        # if message is not decrypted, just print the encrypted message
        if msgData[2] == 0:
            returnMsg = '\nMessage is not decrypted:\nEncrypted message: [' + msgData[1] + ']\n'
            return returnMsg
        # if message is decrypted, print both the encryped message and the decrypted message
        elif msgData[2] == 1:
            returnMsg = '\nMessage is decrypted:\nEncrypted message: [' + msgData[1] + ']\nDecrypted message: [' + msgData[4] + ']\n'
        else:
            pass

# if found, add correct configuration to the possible config table in the bombe db when provided with the correct information
def insertPossibleConfig(day, plugIn, plugOut, activeR1, offset1, activeR2, offset2, activeR3, offset3, reflector):
    try:
        insertConfig = 'INSERT INTO PossibleConfig VALUES (' + str(day) + ', \'' + plugIn + '\', \'' + plugOut + '\', ' + str(activeR1) + ', ' + str(offset1) + ', ' + str(activeR2) + ', ' + str(offset2) + ', ' + str(activeR3) + ', ' + str(offset3) + ', \'' + reflector + '\');'
        b = bombeDB.cursor()
        b.execute(insertConfig)
        b.close()
        bombeDB.commit()
        print('\nInserting possible config into the Bombe database.\n')
    except sqlite3.OperationalError:
        print('\nError when trying to insert values, please check the database connection and/or values being input.\n')
    except sqlite3.IntegrityError:
        print('\nError when trying to insert values, this configuration already exists in the database.\n')

# if found, add correct configuration to the known config table in the bombe db when provided with the correct information
def insertKnownConfig(day, plugIn, plugOut, activeR1, offset1, activeR2, offset2, activeR3, offset3, reflector):
    try:
        insertConfig = 'INSERT INTO KnownConfig VALUES (' + str(day) + ', \'' + plugIn + '\', \'' + plugOut + '\', ' + str(activeR1) + ', ' + str(offset1) + ', ' + str(activeR2) + ', ' + str(offset2) + ', ' + str(activeR3) + ', ' + str(offset3) + ', \'' + reflector + '\');'
        b = bombeDB.cursor()
        b.execute(insertConfig)
        b.close()
        bombeDB.commit()
        print('\nKnown config found, inserting into Bombe database.\n')
    except sqlite3.OperationalError:
        print('\nError when trying to insert values, please check the database connection and/or values being input.\n')
    except sqlite3.IntegrityError:
        print('\nError when trying to insert values, this configuration already exists in the database.\n')

# getting known config from bombe db, this is identical to getSchedule() for enigma, but connected to bombe   
def getKnownConfig(day):
    # get all row items in row matching day input by user
    getConfig = 'SELECT * FROM KnownConfig WHERE Day = ' + str(day)
    b = bombeDB.cursor()
    b.execute(getConfig)
    knownConfig = b.fetchone()
    b.close()
    # if knownConfig is null, notify the user
    if not knownConfig:
        print('No config found for Day ' + str(day))
    else:
        # return known enigma configuration
        return knownConfig

# delete wrong configuration from the bombe db
def deleteWrongConfig(day, plugIn, plugOut, activeR1, offset1, activeR2, offset2, activeR3, offset3, reflector):
    # find configuration in PossibleConfig
    findConfig = 'SELECT * FROM PossibleConfig WHERE Day = ' + str(day) + ' AND PlugIn = \'' + plugIn + '\' AND PlugOut = \'' + plugOut + '\' AND ActiveR1 = ' + str(activeR1) + ' AND Offset1 = ' + str(offset1) + ' AND ActiveR2 = ' + str(activeR2) + ' AND Offset2 = ' + str(offset2) + ' AND ActiveR3 = ' + str(activeR3) + ' AND Offset3 = ' + str(offset3) + ' AND Reflector = \'' + str(reflector) + '\''
    b = bombeDB.cursor()
    b.execute(findConfig)
    foundConfig = b.fetchone()
    b.close()
    # if query result is null, check inputs/connection
    if foundConfig == None:
        print('\nNo result found for this configuration, please check the database connection and/or values being input.\n')
    # if query result is found, delete the row from the database
    else:
        deleteConfig = 'DELETE FROM PossibleConfig WHERE Day = ' + str(day) + ' AND PlugIn = \'' + plugIn + '\' AND PlugOut = \'' + plugOut + '\' AND ActiveR1 = ' + str(activeR1) + ' AND Offset1 = ' + str(offset1) + ' AND ActiveR2 = ' + str(activeR2) + ' AND Offset2 = ' + str(offset2) + ' AND ActiveR3 = ' + str(activeR3) + ' AND Offset3 = ' + str(offset3) + ' AND Reflector = \'' + reflector + '\''
        b = bombeDB.cursor()
        b.execute(deleteConfig)
        b.close()
        bombeDB.commit()
        print('\nWrong config has been deleted from the possible configs in the database.\n')

# close db connection
bombeDB.close()

# Sources:
# help with xlsx file support found at https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/#:~:text=Openpyxl%20is%20a%20Python%20library,changes%20based%20on%20some%20criteria.