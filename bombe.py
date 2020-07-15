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
    engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 0, 0, True)
    engimaMachineOUTPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 0, 0, True)

    inputText = (input("Enter message: ")).upper()
    outputText = engimaMachineINPUT.encrypt(inputText)
    originalMessage = engimaMachineOUTPUT.encrypt(outputText)

    print("Original Message: " + originalMessage)
    print("Encrypted Message: " + outputText)

    #to decrypt throwing weird error not sure why!!!

    inputText = input("Enter the message you would like to decrypt:\t")
    crib="HELLOWORLD"
    found = False
    while(found == False):
        for i in range(5):
            for j in range(5):
                machine = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, int(i), int(j), True)
                outputText = machine.encrypt(inputText)
                if outputText == crib:
                    found = True
                    print("Settings have been found!")
                    print("Settings are: Rotor I at offset: "+ str(i) +" Rotor II at offset: "+ str(j))       
main()

    #enigma machine 1 - test 0-5
    #enigma machine 2 - tests 6-10

"""
message = helloworld
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 0, 0, True) = TJJPKKPXZQ
settings: engimaMachineINPUT = enigma("",[], ROTOR_I, ROTOR_II, REFLECTOR_B, 5, 0, True) = UZHZUYBLRV
"""

