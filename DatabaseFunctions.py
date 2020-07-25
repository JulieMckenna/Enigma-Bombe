# classes of functions to create the enigma/bombe databases and interface with them
# author: Chandler Berry

import sqlite3, openpyxl

class CreateDatabases:
        
    # create the enigma database, this can also be used to reset the database
    def createEnigmaDB(self):
        # drop table if it exists before creating it again
        dropTbl = self.enigma.cursor()
        dropTbl.execute('DROP TABLE IF EXISTS Schedule')
        dropTbl.close()

        # create table script for Schedule table
        sched = '''
        CREATE TABLE Schedule
        (
            Day                 INT         PRIMARY KEY NOT NULL,
            PlugIn              CHAR(10)    NOT NULL,
            PlugOut             CHAR(10)    NOT NULL,
            ActiveR1            INT         NOT NULL,
            Offset1             INT         NOT NULL,
            ActiveR2            INT         NOT NULL,
            Offset2             INT         NOT NULL,
            ActiveR3            INT         NOT NULL,
            Offset3             INT         NOT NULL,
            Reflector           TEXT        NOT NULL
        );
        '''
        # create Schedule table
        s = self.enigma.cursor()
        s.execute(sched)
        s.close()

        print('created enigma database')

    # create the bombe database, this can also be used to reset the database
    def createBombeDB(self):
        # drop tables if they exist before creating them
        tables = ['PossibleConfig', 'KnownConfig', 'CapturedMsg']
        for t in tables:
            tbl = self.bombe.cursor()
            tbl.execute('DROP TABLE IF EXISTS ' + t)
            tbl.close()

        # create table script for PossibleConfig table
        possibleConfig = '''
        CREATE TABLE PossibleConfig
        (
            Day                 INT         PRIMARY KEY NOT NULL,
            ActiveR1            INT         NOT NULL,
            Offset1             INT         NOT NULL,
            ActiveR2            INT         NOT NULL,
            Offset2             INT         NOT NULL,
            Reflector           TEXT        NOT NULL
        );
        '''
        # create PossibleConfig table
        pC = self.bombe.cursor()
        pC.execute(possibleConfig)
        pC.close()

        # create table script for KnownConfig table
        knownConfig = '''
        CREATE TABLE KnownConfig
        (
            Day                 INT         PRIMARY KEY NOT NULL,
            ActiveR1            INT         NOT NULL,
            Offset1             INT         NOT NULL,
            ActiveR2            INT         NOT NULL,
            Offset2             INT         NOT NULL,
            Reflector           TEXT        NOT NULL
        );
        '''
        # create KnownConfig table
        kC = self.bombe.cursor()
        kC.execute(knownConfig)
        kC.close()

        # create table script for CapturedMsg table
        capturedMsg = '''
        CREATE TABLE CapturedMsg
        (
            MessageID       INT     PRIMARY KEY NOT NULL,
            EncryptedMsg    TEXT    NOT NULL,
            IsDecrypted     INT     NOT NULL,
            DecryptedMsg    TEXT,
            Day             INT     NOT NULL
        );
        '''        
        # create CapturedMsg table
        capMsg = self.bombe.cursor()
        capMsg.execute(capturedMsg)
        capMsg.close()

        print('created bombe database')

    # initialize class
    def __init__(self):
        # create enigma db connection
        self.enigma = sqlite3.connect('EnigmaDB.db')
        print('enigma database connection established')
        # create bombe db connection
        self.bombe = sqlite3.connect('BombeDB.db')
        print('bombe database connection established\n')

    # close db connections
    def __del__(self):
        self.enigma.close()
        print('\nenigma database connection closed')
        self.bombe.close()
        print('bombe database connection closed')


class EnigmaDatabase: 
    
    # initialize class
    def __init__(self):
        # create enigma db connection
        self.connection = sqlite3.connect('EnigmaDB.db')
        print('enigma database connection established')

    # add enigma schedule to db with data provided by an excel file
    # file path of test file (Chandler) --- 'G:\\gitrepos\\Enigma-Bombe\\enigma.xlsx'
    def createEnigmaSchedule(self, filePath):
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
            e = self.connection.cursor()
            e.execute(insertConfig)
            print('Config for day ' + str(getConfig[0]) + ' inserted into db.')
            e.close()
            self.connection.commit()

    # get schedule from enigma database when function is provided with a day
    def getConfiguration(self, day):
        # get all row items in row matching day input by user
        getSched = 'SELECT * FROM Schedule WHERE Day = ' + str(day)
        e = self.connection.cursor()
        e.execute(getSched)
        schedResult = e.fetchone()
        e.close()
        # if schedResult is null, notify the user
        if not schedResult:
            print('No config found for Day ' + str(day))
            configuration = None
        else:
            # save plugboard setting 
            plugString = schedResult[1][0] + schedResult[2][0] + ',' + schedResult[1][1] + schedResult[2][1] + ',' + schedResult[1][2] + schedResult[2][2] + ',' + schedResult[1][3] + schedResult[2][3] + ',' + schedResult[1][4] + schedResult[2][4] + ',' + schedResult[1][5] + schedResult[2][5] + ',' + schedResult[1][6] + schedResult[2][6] + ',' + schedResult[1][7] + schedResult[2][7] + ',' + schedResult[1][8] + schedResult[2][8] + ',' + schedResult[1][9] + schedResult[2][9]
            # save list of settings in a usable format for the rest of enigma
            configuration = (schedResult[0], plugString, schedResult[3], schedResult[4], schedResult[5], schedResult[6], schedResult[7], schedResult[8], schedResult[9])
            # return enigma configuration
        return configuration

    # close db connection
    def __del__(self):
        self.connection.close()
        print('enigma database connection closed')

class BombeDatabase:

    # initialize class
    def __init__(self): 
        # create bombe db connection
        self.connection = sqlite3.connect('BombeDB.db')
        print('bombe database connection established')

    # insert message captured into database
    def insertCapturedMsg(self, msg, day):
        try:
            # logic to create new message ID
            # get the largest value message ID that is stored in the database, if there are no messages stored, this query will return null
            getMsgID = 'SELECT MAX(MessageID) FROM CapturedMsg'
            b = self.connection.cursor()
            b.execute(getMsgID)
            msgID = b.fetchone()
            b.close()
            newID = None
            # if there are no messages stored in the database, then the message ID will be 1
            if msgID[0] == None:
                newID = 1
            # if there are messages stored in the database, then take the largest value message ID and add 1
            else:
                newID = msgID[0] + 1
            # insert new captured message into the database
            insertMessage = 'INSERT INTO CapturedMsg VALUES (' + str(newID) + ', \'' + msg + '\', 0, NULL, ' + str(day) + ');'
            b = self.connection.cursor()
            b.execute(insertMessage)
            b.close()
            self.connection.commit()
            print('Message saved.')
        except sqlite3.OperationalError:
            print('\nError when trying to insert values, please check the database connection and/or values being input.\n')
        except sqlite3.IntegrityError:
            print('\nError when trying to insert values, this configuration already exists in the database.\n')

    # get CapturedMsg from bombe db
    def getCapturedMsg(self, msgID):
        # find message in database with matching message id
        getMessage = 'SELECT * FROM CapturedMsg WHERE MessageID = ' + str(msgID)
        b = self.connection.cursor()
        b.execute(getMessage)
        msgData = b.fetchone()
        b.close()
        # if message is not found, print that to the user
        if msgData == None:
            returnMsg = 'No message in database with that ID.'
        else:
            # if message is not decrypted, just print the encrypted message
            if msgData[2] == 0:
                returnMsg = '\nMessage is not decrypted:\nEncrypted message: [' + msgData[1] + ']\n'
            # if message is decrypted, print both the encryped message and the decrypted message
            elif msgData[2] == 1:
                returnMsg = '\nMessage is decrypted:\nEncrypted message: [' + msgData[1] + ']\nDecrypted message: [' + msgData[4] + ']\n'
        return returnMsg

    # if found, add correct configuration to the possible config table in the bombe db when provided with the correct information
    def insertPossibleConfig(self, day, activeR1, offset1, activeR2, offset2, reflector):
        try:
            insertConfig = 'INSERT INTO PossibleConfig VALUES (' + str(day) + ', ' + str(activeR1) + ', ' + str(offset1) + ', ' + str(activeR2) + ', ' + str(offset2) + ', \'' + reflector + '\');'
            b = self.connection.cursor()
            b.execute(insertConfig)
            b.close()
            self.connection.commit()
            print('\nInserting possible config into the Bombe database.\n')
        except sqlite3.OperationalError:
            print('\nError when trying to insert values, please check the database connection and/or values being input.\n')
        except sqlite3.IntegrityError:
            print('\nError when trying to insert values, this configuration already exists in the database.\n')

    # if found, add correct configuration to the known config table in the bombe db when provided with the correct information
    def insertKnownConfig(self, day, activeR1, offset1, activeR2, offset2, reflector):
        try:
            insertConfig = 'INSERT INTO KnownConfig VALUES (' + str(day) + ', ' + str(activeR1) + ', ' + str(offset1) + ', ' + str(activeR2) + ', ' + str(offset2) + ', \'' + reflector + '\');'
            b = self.connection.cursor()
            b.execute(insertConfig)
            b.close()
            self.connection.commit()
            print('\nKnown config found, inserting into Bombe database.\n')
        except sqlite3.OperationalError:
            print('\nError when trying to insert values, please check the database connection and/or values being input.\n')
        except sqlite3.IntegrityError:
            print('\nError when trying to insert values, this configuration already exists in the database.\n')

    # getting known config from bombe db, this is identical to getSchedule() for enigma, but connected to bombe   
    def getKnownConfig(self, day):
        # get all row items in row matching day input by user
        getConfig = 'SELECT * FROM KnownConfig WHERE Day = ' + str(day)
        b = self.connection.cursor()
        b.execute(getConfig)
        knownConfig = b.fetchone()
        b.close()
        # if knownConfig is null, notify the user
        if not knownConfig:
            print('No config found for Day ' + str(day))
            return None
        else:
            # return known enigma configuration
            return knownConfig

    # delete wrong configuration from the bombe db
    def deleteWrongConfig(self, day, activeR1, offset1, activeR2, offset2, reflector):
        # find configuration in PossibleConfig
        findConfig = 'SELECT * FROM PossibleConfig WHERE Day = ' + str(day) + ' AND ActiveR1 = ' + str(activeR1) + ' AND Offset1 = ' + str(offset1) + ' AND ActiveR2 = ' + str(activeR2) + ' AND Offset2 = ' + str(offset2) + ' AND Reflector = \'' + str(reflector) + '\''
        b = self.connection.cursor()
        b.execute(findConfig)
        foundConfig = b.fetchone()
        b.close()
        # if query result is null, check inputs/connection
        if foundConfig == None:
            print('\nNo result found for this configuration, please check the database connection and/or values being input.\n')
        # if query result is found, delete the row from the database
        else:
            deleteConfig = 'DELETE FROM PossibleConfig WHERE Day = ' + str(day) + ' AND ActiveR1 = ' + str(activeR1) + ' AND Offset1 = ' + str(offset1) + ' AND ActiveR2 = ' + str(activeR2) + ' AND Offset2 = ' + str(offset2) + ' AND Reflector = \'' + reflector + '\''
            b = self.connection.cursor()
            b.execute(deleteConfig)
            b.close()
            self.connection.commit()
            print('\nWrong config has been deleted from the possible configs in the database.\n')

    # close db connection
    def __del__(self):
        self.connection.close()
        print('bombe database connection closed')

# Sources:
# help with xlsx file support found at https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/#:~:text=Openpyxl%20is%20a%20Python%20library,changes%20based%20on%20some%20criteria.
# destructors in python: https://www.geeksforgeeks.org/destructors-in-python/
