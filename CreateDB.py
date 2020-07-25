# run this to create/reset the enigma and bombe databases
import DatabaseFunctions
db = DatabaseFunctions.CreateDatabases()
db.createBombeDB()
db.createEnigmaDB()
del db

i = input('insert default enigma schedule? (y/n): ')
if i.upper() == 'Y':
    e_db = DatabaseFunctions.EnigmaDatabase()
    e_db.createEnigmaSchedule('G:\\gitrepos\\Enigma-Bombe\\enigma.xlsx')
    del e_db
elif i.upper() == 'N':
    exit()
else:
    pass