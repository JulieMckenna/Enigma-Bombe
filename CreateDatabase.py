# script to create the db tables, can be used to reset the db if necessary
# author: Chandler Berry

import sqlite3

##### BOMBE #####
# open db connection for Bombe
bombeDB = sqlite3.connect('Bombe.db')

# drop tables if they exist before creating them
tables = ['PossibleConfig', 'KnownConfig', 'WrongConfig', 'CapturedMsg']
for t in tables:
    tbl = bombeDB.cursor()
    tbl.execute('DROP TABLE IF EXISTS ' + t)
    tbl.close()

# create table script for PossibleConfig table
possibleConfig = '''
CREATE TABLE PossibleConfig
(
    ConfigID    INT     PRIMARY KEY NOT NULL,
    PlugIn      TEXT    NOT NULL,
    PlugOut     TEXT    NOT NULL,
    RotorOne    CHAR(1),
    RotorTwo    CHAR(1),
    RotorThree  CHAR(1),
    RotorFour   CHAR(1),
    RotorFive   CHAR(1),
    Reflector   INT     NOT NULL,
    DayOfMonth  INT     NOT NULL
);
'''
# create PossibleConfig table
pC = bombeDB.cursor()
pC.execute(possibleConfig)
pC.close()

# create table script for KnownConfig table
knownConfig = '''
CREATE TABLE CapturedMsg
(
    MessageID       INT     PRIMARY KEY NOT NULL,
    EncryptedMsg    TEXT    NOT NULL,
    IsDecrypted     INT     NOT NULL,
    DecryptedMsg    TEXT,
    Day             INT     NOT NULL
);
'''
# create KnownConfig table
kC = bombeDB.cursor()
kC.execute(knownConfig)
kC.close()

# create table script for WrongConfig table
wrongConfig = '''
CREATE TABLE WrongConfig
(
    ConfigID        INT     PRIMARY KEY NOT NULL,
    PlugIn          TEXT    NOT NULL,
    PlugOut         TEXT    NOT NULL,
    RotorOne        CHAR(1),
    RotorTwo        CHAR(1),
    RotorThree      CHAR(1),
    RotorFour       CHAR(1),
    RotorFive       CHAR(1),
    Reflector       INT     NOT NULL,
    DayOfMonth      INT     NOT NULL
);
'''
# create WrongConfig table
wC = bombeDB.cursor()
wC.execute(wrongConfig)
wC.close()

# create table script for CapturedMsg table
capturedMsg = '''
CREATE TABLE KnownConfig
(
    ConfigID            INT     PRIMARY KEY NOT NULL,
    PlugIn              TEXT    NOT NULL,
    PlugOut             TEXT    NOT NULL,
    RotorOne            CHAR(1),
    RotorTwo            CHAR(1),
    RotorThree          CHAR(1),
    RotorFour           CHAR(1),
    RotorFive           CHAR(1),
    Reflector           INT     NOT NULL,
    DayOfMonth          INT     NOT NULL,
    TransposedAlphabet  TEXT    NOT NULL
);
'''
# create CapturedMsg table
capMsg = bombeDB.cursor()
capMsg.execute(capturedMsg)
capMsg.close()

#close the db connection
bombeDB.close()

print('Created Bombe Database')

##### ENIGMA #####
# open db connection for Enigma
enigmaDB = sqlite3.connect('Enigma.db')

# drop table if it exists before creating it again
dropTbl = enigmaDB.cursor()
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
    Reflector           CHAR(1)     NOT NULL
);
'''
# create Schedule table
s = enigmaDB.cursor()
s.execute(sched)
s.close()

# close the db connection
enigmaDB.close()

print('Created Enigma Database')