# classes of functions to create the enigma/bombe databases and interface with them
# author: Chandler Berry

import sqlite3, os

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

        insert = self.enigma.cursor()
        configs = [(1, 'ABCDEFGHIJ', 'LMNOPQRSTU', 1, 17, 2, 3, 4, 2, 'B'), (2, 'LMNOPQRSTU', 'ABCDEFGHIJ', 3, 13, 2, 16, 4, 2, 'B'), (3, 'QWERTYUIOP', 'LKJHGFDSAZ', 5, 14, 3, 11, 1, 5, 'B'), (4, 'ZXCVBNMLKJ', 'HGFDSAPOIU', 3, 4, 1, 12, 3, 16, 'B'), (5, 'QAZWSXEDCR', 'FVTGBYHNUJ', 2, 18, 4, 14, 3, 8, 'B'), (6, 'QZECTBUMIL', 'PLOKIJUHYG', 1, 2, 3, 25, 4, 22, 'B'), (7, 'ALQPWODJUR', 'NTIGFUDOWQ', 4, 25, 2, 15, 5, 5, 'B'), (8, 'LSIDUCBKEQ', 'UBHVGYCXTA', 5, 11, 3, 2, 1, 11, 'B'), (9, 'PQLAMZSUDI', 'YUIKJHBNML', 2, 5, 5, 11, 3, 18, 'B'), (10, 'EORPFLSABN', 'DOFVKCLXQM', 4, 12, 2, 24, 5, 6, 'B')]
        for c in configs:
            insert.execute('INSERT INTO Schedule VALUES (' + str(c[0]) + ', \'' + c[1] + '\', \'' + c[2] + '\', ' + str(c[3]) + ', ' + str(c[4]) + ', ' + str(c[5]) + ', ' + str(c[6]) + ', ' + str(c[7]) + ', ' + str(c[8]) + ', \'' + c[9] + '\');')
        insert.close()
        self.enigma.commit()
        print('created enigma database')

    # create the bombe database, this can also be used to reset the database
    def createBombeDB(self):
        # drop tables if they exist before creating them
        tables = ['KnownConfig', 'CapturedMsg']
        for t in tables:
            tbl = self.bombe.cursor()
            tbl.execute('DROP TABLE IF EXISTS ' + t)
            tbl.close()

        # create table script for KnownConfig table
        knownConfig = '''
        CREATE TABLE KnownConfig
        (
            ID                  INT         PRIMARY KEY NOT NULL,
            ActiveR1            INT         NOT NULL,
            Offset1             INT         NOT NULL,
            ActiveR2            INT         NOT NULL,
            Offset2             INT         NOT NULL,
            ActiveR3            INT         NOT NULL,
            Offset3             INT         NOT NULL,
            Reflector           TEXT        NOT NULL
        );
        '''
        # create KnownConfig table
        kC = self.bombe.cursor()
        kC.execute(knownConfig)
        kC.close()

        print('created bombe database')

    # initialize class, refresh databases
    def __init__(self):
        # delete pre-existing db files
        dbNames = ['EnigmaDB.db', 'BombeDB.db']
        for file in dbNames:
            if os.path.exists(file):
                os.remove(file)
        # create enigma db connection
        self.enigma = sqlite3.connect('EnigmaDB.db')
        print('enigma database connection established')
        self.createEnigmaDB()
        print('Enigma database created')
        # create bombe db connection
        self.bombe = sqlite3.connect('BombeDB.db')
        print('bombe database connection established\n')
        self.createBombeDB()
        print('Bombe database created')

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

    # insert the correct configuration when it is found by the bombe machine
    def insertKnownConfig(self, activeR1, offset1, activeR2, offset2, activeR3, offset3, reflector):
        try:
            # create ID for primary key of db tuple
            getMaxConfigID = 'SELECT MAX(ID) FROM KnownConfig'
            b = self.connection.cursor()
            b.execute(getMaxConfigID)
            maxID = b.fetchone()
            b.close()
            newID = None
            # if there are no known configurations stored in the database, then the ID will be 1
            if maxID[0] == None:
                newID = 1
            # if there are known configurations stored in the database, then take the largest value ID and add 1
            else:
                newID = maxID[0] + 1
            insertConfig = 'INSERT INTO KnownConfig VALUES (' + str(newID) + ', ' + str(activeR1) + ', ' + str(offset1) + ', ' + str(activeR2) + ', ' + str(offset2) + ', ' + str(activeR3) + ', ' + str(offset3) + ', \'' + reflector + '\');'
            b = self.connection.cursor()
            b.execute(insertConfig)
            b.close()
            self.connection.commit()
            print('Settings have been found! Saving configuartion in database.')
        except sqlite3.OperationalError:
            print('\nError when trying to insert values, please check the database connection and/or values being input.\n')
        except sqlite3.IntegrityError:
            print('\nError when trying to insert values, this configuration already exists in the database.\n')

    # getting known config from bombe db 
    def getKnownConfig(self, activeR1, offset1, activeR2, offset2, activeR3, offset3, reflector):
        # get all row items in row matching day input by user
        getConfig = 'SELECT * FROM KnownConfig WHERE ActiveR1 = ' + str(activeR1) + ' AND Offset1 = ' + str(offset1) + ' AND ActiveR2 = ' + str(activeR2) + ' AND Offset2 = ' + str(offset2) + ' AND ActiveR3 = ' + str(activeR3) + ' AND Offset3 = ' + str(offset3)
        b = self.connection.cursor()
        b.execute(getConfig)
        knownConfig = b.fetchone()
        b.close()
        # if knownConfig is null, notify the user
        if knownConfig == None:
            print('No config found for these settings')
            return None
        else:
            # return known enigma configuration
            return knownConfig

    # close db connection
    def __del__(self):
        self.connection.close()
        print('bombe database connection closed')

# Sources:
# help with xlsx file support found at https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/#:~:text=Openpyxl%20is%20a%20Python%20library,changes%20based%20on%20some%20criteria.
# destructors in python: https://www.geeksforgeeks.org/destructors-in-python/
