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
    engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 1, 2, True)
    engimaMachineOUTPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 1, 2, True)

    inputText = (input("Enter message: ")).upper()
    #inputText += "HELLOWORLD"
    outputText = engimaMachineINPUT.encrypt(inputText)
    originalMessage = engimaMachineOUTPUT.encrypt(outputText)

    print("Original Message: " + originalMessage)
    print("Encrypted Message: " + outputText)

    #to decrypt throwing weird error not sure why!!!

    inputText = input("Enter the message you would like to decrypt:\t").upper()
    #usermessgae = inputText[0:(len(inputText)-10)]
    #print(usermessgae)
    #helloworld = inputText[(len(inputText)-10):]
    #print(helloworld)

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
                    #decryptedmessage = machine.encrypt(usermessgae) 
                del machine 
                """
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
                """
main()


"""
message = helloworld
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 0, 0, True) = TJJPKKPXZQ
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 0, 0, True) = DBWHTDPGJA
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 5, 0, True) = UZHZUYBLRV
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 6, 2, True) = EIQJJPVVAF
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 17, 3, True) = ZFMKRERTWH
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 21, 3, True) = SWXODXQEIZ
DBWHTEIQJJPVVAF
"""

