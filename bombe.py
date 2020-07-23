from Enigma2 import enigma

#Bombe
"""
steps of to create - will be simplier than an actual Bombe machine
1. 2 rotors - know the which rotors but no their position(limited positions(0-10))
2. add in 5 plug board connections
3. add in full possition range
4. add in 3rd rotos - if we get to it
"""


ROTOR_I =   "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II =  "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
## A comes out of R3 then goes to the reflector
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
REFLECTOR_A = "EDCHIJKLMNOPQRSTUVWZYZABGF"

#will have 2 enigma machines running at once. One will take setting 1 half of positions

def main():
    #find possible encryptions first - to then solve with decrption 
    engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 17, 3, True)
    engimaMachineOUTPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 17, 3, True)

    inputText = (input("Enter message: ")).upper()
    outputText = engimaMachineINPUT.encrypt(inputText)
    originalMessage = engimaMachineOUTPUT.encrypt(outputText)

    print("Original Message: " + originalMessage)
    print("Encrypted Message: " + outputText)

    #to decrypt throwing weird error not sure why!!!

    inputText = input("Enter the message you would like to decrypt:\t").upper()
    crib="HELLOWORLD"
    found = False
    while(found == False):
        for i in range(5):
            for j in range(26):
                machine = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, int(i), int(j), True)
                outputText = machine.encrypt(inputText)
                if outputText == crib:
                    found = True
                    print("Settings have been found!")
                    print("Settings are: Rotor I at offset: "+ str(i) +" Rotor II at offset: "+ str(j)) 
                del machine 
        for i in range(6,10):
            for j in range(26):
                machine = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, int(i), int(j), True)
                outputText = machine.encrypt(inputText)
                if outputText == crib:
                    found = True
                    print("Settings have been found!")
                    print("Settings are: Rotor I at offset: "+ str(i) +" Rotor II at offset: "+ str(j))
                del machine
        for i in range(11,15):
            for j in range(26):
                machine = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, int(i), int(j), True)
                outputText = machine.encrypt(inputText)
                if outputText == crib:
                    found = True
                    print("Settings have been found!")
                    print("Settings are: Rotor I at offset: "+ str(i) +" Rotor II at offset: "+ str(j)) 
                del machine
        for i in range(16,20):
            for j in range(10):
                machine = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, int(i), int(j), True)
                outputText = machine.encrypt(inputText)
                if outputText == crib:
                    found = True
                    print("Settings have been found!")
                    print("Settings are: Rotor I at offset: "+ str(i) +" Rotor II at offset: "+ str(j))  
                del machine 
        for i in range(21,26):
            for j in range(26):
                machine = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, int(i), int(j), True)
                outputText = machine.encrypt(inputText)
                if outputText == crib:
                    found = True
                    print("Settings have been found!")
                    print("Settings are: Rotor I at offset: "+ str(i) +" Rotor II at offset: "+ str(j))   
                del machine  
main()

    #enigma machine 1 - test 0-5
    #enigma machine 2 - tests 6-10

"""
message = helloworld
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 0, 0, True) = TJJPKKPXZQ
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 5, 0, True) = UZHZUYBLRV
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 6, 2, True) = EIQJJPVVAF
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 17, 3, True) = ZFMKRERTWH
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 21, 3, True) = SWXODXQEIZ
"""



## Current Bombe goal:
    ## 2 rotor machine, solve for offset of each
    ## 1 Rotor is known, solve for the other rotor
        ## Rotor options could be however many you want
    ## Want to get everythign in Bombe working and scale up as much as possible
