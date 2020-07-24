# run this to create or refresh the enigma and bombe databases
import DatabaseFunctions
db = DatabaseFunctions.CreateDatabases()
db.createBombeDB()
db.createEnigmaDB()
del db
