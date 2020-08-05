from enigma import enigma
import DatabaseFunctions


ROTOR_I =   "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II =  "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

## A comes out of R3 then goes to the reflector
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
REFLECTOR_A = "EDCHIJKLMNOPQRSTUVWZYZABGF"

#will have multiple enigma machines running at once. One will take setting 1 half of positions

def retrivesettings():
    global s
    ns = s
    return ns
def retrivemessage():
    global s
    nm = m
    return nm
def setsettings(finalsettings):
    global s
    s = finalsettings
def setmessage(finalmessage):
    global m
    m = finalmessage

def setstatus(flag1):
    global flag
    flag = flag1
    return

def getstatus():
    global flag
    flag1 = flag
    return flag1
def settries(num):
    global tries
    tries = num
    return
def gettries():
    global tries
    tries1 = tries
    return tries1
def bombe3(emessage,rotorptwo,rotorpone,rotorpzero):
    global s
    global m
    global flag
    flag = True
    global tries
    numOfAttempts = 0
    reflector = REFLECTOR_B
    #find possible encryptions first - to then solve with decrption
    inputText = emessage
    #adds this to end of the message - to use to solve fo rthe crib
    #gets the encoded message - to then "break" with Bombe



    #to decrypt throwing weird error not sure why!!!

    crib="HELLOWORLD"
    for i in range(0, 6):
        for j in range(0, 26):
            for k in range(0, 26):
                numOfAttempts += 1
                #makes a machine with the varied settings
                machine = enigma("",[], rotorptwo, rotorpone, rotorpzero, reflector, int(i), int(j), int(k), False)
                outputText = machine.encrypt(inputText)
                #checks if th last 10 letters of the "decrypted" message = helloworld
                if outputText[(len(inputText)-10):] == crib:
                    #means that the correct settings have been found
                    #print("Settings have been found!")
                    #finalsettings = "Off1: " + str(i) + " Off2: " + str(j) + " Off3: " + str(k)
                    finalsettings = " Off3: " + str(k) + " Off2: " + str(j) + " Off1: " + str(i)
                    setsettings(finalsettings)
                    # prints the decrypted message
                    finalmessage = outputText[0:(len(outputText) - 10)]
                    setmessage(finalmessage)
                    b_db = DatabaseFunctions.BombeDatabase()
                    b_db.insertKnownConfig(1, str(i), 2, str(j), 3, str(k), 'B', finalmessage)
                    settingsList = b_db.getKnownConfig(1, str(i), 2, str(j), 3, str(k), 'B')
                    print("Settings are: Rotor I at offset: "+ str(settingsList[2]) +" Rotor II at offset: "+ str(settingsList[4]) + " Rotor III at offset: " + str(settingsList[6]))
                    del b_db
                    settries(numOfAttempts)
                    print("Number of combinations tried: " + str(numOfAttempts))
                    return
                del machine
    for i in range(6,11):
        for j in range(0, 26):
            for k in range(0, 26):
                numOfAttempts += 1
                #makes a machine with the varied settings
                machine = enigma("",[], rotorptwo, rotorpone, rotorpzero, reflector, int(i), int(j), int(k), False)
                outputText = machine.encrypt(inputText)
                #checks if th last 10 letters of the "decrypted" message = helloworld
                if outputText[(len(inputText)-10):] == crib:
                    #means that the correct settings have been found
                    #finalsettings = "Off1: " + str(i) + " Off2: " + str(j) + " Off3: " + str(k)
                    finalsettings = " Off3: " + str(k) + " Off2: " + str(j) + " Off1: " + str(i)
                    setsettings(finalsettings)
                    # prints the decrypted message
                    finalmessage = outputText[0:(len(outputText) - 10)]
                    setmessage(finalmessage)
                    b_db = DatabaseFunctions.BombeDatabase()
                    b_db.insertKnownConfig(1, str(i), 2, str(j), 3, str(k), 'B', finalmessage)
                    settingsList = b_db.getKnownConfig(1, str(i), 2, str(j), 3, str(k), 'B')
                    print("Settings are: Rotor I at offset: "+ str(settingsList[2]) +" Rotor II at offset: "+ str(settingsList[4]) + " Rotor III at offset: " + str(settingsList[6]))
                    del b_db
                    settries(numOfAttempts)
                    print("Number of combinations tried: " + str(numOfAttempts))
                    return
                del machine
    for i in range(11,16):
        for j in range(0, 26):
            for k in range(0, 26):
                numOfAttempts += 1
                #makes a machine with the varied settings
                machine = enigma("",[], rotorptwo, rotorpone, rotorpzero, reflector, int(i), int(j), int(k), False)
                outputText = machine.encrypt(inputText)
                #checks if th last 10 letters of the "decrypted" message = helloworld
                if outputText[(len(inputText)-10):] == crib:
                    #means that the correct settings have been found
                    #finalsettings = "Off1: " + str(i) + " Off2: " + str(j) + " Off3: " + str(k)
                    finalsettings = " Off3: " + str(k) + " Off2: " + str(j) + " Off1: " + str(i)
                    setsettings(finalsettings)
                    # prints the decrypted message
                    finalmessage = outputText[0:(len(outputText) - 10)]
                    setmessage(finalmessage)
                    b_db = DatabaseFunctions.BombeDatabase()
                    b_db.insertKnownConfig(1, str(i), 2, str(j), 3, str(k), 'B', finalmessage)
                    settingsList = b_db.getKnownConfig(1, str(i), 2, str(j), 3, str(k), 'B')
                    print("Settings are: Rotor I at offset: "+ str(settingsList[2]) +" Rotor II at offset: "+ str(settingsList[4]) + " Rotor III at offset: " + str(settingsList[6]))
                    del b_db
                    settries(numOfAttempts)
                    print("Number of combinations tried: " + str(numOfAttempts))
                    return
                del machine
    for i in range(16,21):
        for j in range(0, 26):
            for k in range(0, 26):
                numOfAttempts += 1
                #makes a machine with the varied settings
                machine = enigma("",[], rotorptwo, rotorpone, rotorpzero, reflector, int(i), int(j), int(k), False)
                outputText = machine.encrypt(inputText)
                #checks if th last 10 letters of the "decrypted" message = helloworld
                if outputText[(len(inputText)-10):] == crib:
                    #means that the correct settings have been found
                    #finalsettings = "Off1: " + str(i) + " Off2: " + str(j) + " Off3: " + str(k)
                    finalsettings = " Off3: " + str(k) + " Off2: " + str(j) + " Off1: " + str(i)
                    setsettings(finalsettings)
                   # prints the decrypted message
                    finalmessage = outputText[0:(len(outputText) - 10)]
                    setmessage(finalmessage)
                    b_db = DatabaseFunctions.BombeDatabase()
                    b_db.insertKnownConfig(1, str(i), 2, str(j), 3, str(k), 'B', finalmessage)
                    settingsList = b_db.getKnownConfig(1, str(i), 2, str(j), 3, str(k), 'B')
                    print("Settings are: Rotor I at offset: "+ str(settingsList[2]) +" Rotor II at offset: "+ str(settingsList[4]) + " Rotor III at offset: " + str(settingsList[6]))
                    del b_db
                    settries(numOfAttempts)
                    print("Number of combinations tried: " + str(numOfAttempts))
                    return
                del machine
    for i in range(21,26):
        for j in range(0, 26):
            for k in range(0, 26):
                numOfAttempts += 1
                #makes a machine with the varied settings
                machine = enigma("",[], rotorptwo, rotorpone, rotorpzero, reflector, int(i), int(j), int(k), False)
                outputText = machine.encrypt(inputText)
                #checks if th last 10 letters of the "decrypted" message = helloworld
                if outputText[(len(inputText)-10):] == crib:
                    #means that the correct settings have been found
                    #finalsettings = "Off1: " + str(i) + " Off2: " + str(j) + " Off3: " + str(k)
                    finalsettings = " Off3: " + str(k) + " Off2: " + str(j) + " Off1: " + str(i)
                    setsettings(finalsettings)
                    # prints the decrypted message
                    finalmessage = outputText[0:(len(outputText) - 10)]
                    setmessage(finalmessage)
                    b_db = DatabaseFunctions.BombeDatabase()
                    b_db.insertKnownConfig(1, str(i), 2, str(j), 3, str(k), 'B', finalmessage)
                    settingsList = b_db.getKnownConfig(1, str(i), 2, str(j), 3, str(k), 'B')
                    print("Settings are: Rotor I at offset: "+ str(settingsList[2]) +" Rotor II at offset: "+ str(settingsList[4]) + " Rotor III at offset: " + str(settingsList[6]))
                    del b_db
                    settries(numOfAttempts)
                    print("Number of combinations tried: " + str(numOfAttempts))
                    return
                del machine
    print("Nothing found")
    flag = False
    setstatus(flag)



#main()


"""
message = helloworld
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 0, 0, True) = TJJPKKPXZQ
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 0, 0, True) = DBWHTDPGJA
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 5, 0, True) = UZHZUYBLRV
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 6, 2, True) = EIQJJPVVAF
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 17, 3, True) = ZFMKRERTWH
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 21, 3, True) = SWXODXQEIZ
DBWHTEIQJJPVVAF
fgpxcfgzmuiklyz
"""



## Current Bombe goal:
    ## 2 rotor machine, solve for offset of each
    ## 1 Rotor is known, solve for the other rotor
        ## Rotor options could be however many you want
