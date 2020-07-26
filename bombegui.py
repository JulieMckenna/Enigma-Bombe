from enigma import enigma
from Main import *

ROTOR_I =   "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II =  "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

## A comes out of R3 then goes to the reflector
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
REFLECTOR_A = "EDCHIJKLMNOPQRSTUVWZYZABGF"

#will have multiple enigma machines running at once. One will take setting 1 half of positions
global finalsettings
global finalmessage


def retrivesettings():
    return finalsettings
def retrivemessage():
    return finalmessage


def bombe3(emessage,rotorptwo,rotorpone,rotorpzero):
    numOfAttempts = 0
    reflector = REFLECTOR_B
    #find possible encryptions first - to then solve with decrption
    inputText = emessage
    #adds this to end of the message - to use to solve fo rthe crib
    inputText += "HELLOWORLD"
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
                    finalsettings = "Off1 " + str(i) + "Off2 " + str(j) + "Off3: " + str(k)
                    setcombo(finalsettings)
                    # this is where the insert query
                    # prints the decrypted message
                    finalmessage = outputText[0:(len(outputText) - 10)]
                    setdecrpt(finalmessage)
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
                    finalsettings = "Off1 " + str(i) + "Off2 " + str(j) + "Off3: " + str(k)
                    setcombo(finalsettings)
                    # this is where the insert query
                    # prints the decrypted message
                    finalmessage = outputText[0:(len(outputText) - 10)]
                    setdecrpt(finalmessage)
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
                    finalsettings = "Off1 " + str(i) + "Off2 " + str(j) + "Off3: " + str(k)
                    setcombo(finalsettings)
                    # this is where the insert query
                    # prints the decrypted message
                    finalmessage = outputText[0:(len(outputText) - 10)]
                    setdecrpt(finalmessage)
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
                    finalsettings = "Off1 " + str(i) + "Off2 " + str(j) + "Off3: " + str(k)
                    setcombo(finalsettings)
                    # this is where the insert query
                    # prints the decrypted message
                    finalmessage = outputText[0:(len(outputText) - 10)]
                    setdecrpt(finalmessage)
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
                    finalsettings = "Off1 " + str(i) + "Off2 " + str(j) + "Off3: " + str(k)
                    setcombo(finalsettings)
                    # this is where the insert query
                    # prints the decrypted message
                    finalmessage = outputText[0:(len(outputText) - 10)]
                    setdecrpt(finalmessage)
                    print("Number of combinations tried: " + str(numOfAttempts))
                    return
                del machine
    finalmessage="Nothing found"
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
