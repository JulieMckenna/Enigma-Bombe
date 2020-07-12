################## NOTES #################

## 1. Need to figure out the rotor offset. index = ord(text[i + self.r1]) % 65 ????



class enigma:
    rotor1 = ""
    rotor2 = ""
    rotor3 = ""
    reflector = ""

    def __init__(self, rotor1, rotor2, rotor3, reflector, offset1, offset2, offset3):
        
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflector = reflector

        ## Setup the rotor with the offset taken into account
        ## If the rotor was "ABCD" with an offset of 2, the new rotor would be "DCAB"
        ## So, the rotor of "ABCD" starts at position 2 of the string, and is looped like a wheel/rotor

        for i in range(0, offset1):
            self.rotor1 = self.stepRotorBack(self.rotor1)

        for i in range(0, offset2):
            self.rotor2 = self.stepRotorBack(self.rotor2)

        for i in range(0, offset3):
            self.rotor3 = self.stepRotorBack(self.rotor3)


    ## Function to step rotor by 1 position
    ## Input is the rotor string
    ## Each char needs to move right by 1, and the last char needs to go into the first position
    def stepRotor(self, rotor):
        #print("Stepping rotor by 1 place")
        ## Save last char
        lastChar = rotor[25]
        returnString = rotor[25]
        ## Move each char forward 1 position
        for i in range(0, len(rotor) - 1):
            rotorAsList = list(rotor)
            tempChar = rotorAsList[i]
            rotorAsList[i + 1] = tempChar
            returnString += rotorAsList[i + 1]
        #print(returnString)
        return returnString

    def stepRotorBack(self, rotor):
        #print("Stepping rotor back by 1")
        firstChar = rotor[0]
        returnString = ""

        for i in range(1, len(rotor)):
            rotorAsList = list(rotor)
            tempChar = rotorAsList[i]
            rotorAsList[i-1] = tempChar
            returnString += rotorAsList[i-1]
        returnString += firstChar
        return returnString

    def encrypt(self, text):



        
        ## Count for how many times each rotor is stepped. Don't care how many times rotor3 is stepped
        r1_count = 0
        r2_count = 0


        returnString = ""

        ##print("Rotor I: " + self.rotor1)
        ##print("Rotor II: " + self.rotor2)
        ##print("Rotor III: " + self.rotor3)
        ##print("Initial String: " + text)


        ## Loop through each character of the text provided
        for i in range(0, len(text)):
            ## Step rotor 1 every iteration
            self.rotor1 = self.stepRotorBack(self.rotor1)

            ## Step rotor 2 if rotor 1 has been stepped 26 times
            if(r1_count == 25):
                self.rotor2 = self.stepRotorBack(self.rotor2)
                r1_count = 0
                r2_count += 1
            ## Step rotor 3 if rotor 2 has been stepped 26 times
            if(r2_count == 25):
                r2_count = 0
                self.rotor3 = self.stepRotorBack(self.rotor3)


            r1_count += 1

            ## Find the index of the current char (CHAR % 65) should give index of an uppercase character
            ## ord(char) returns unicode of character

            ## Find character routing from index of text[i]
            ## charOne is the output from rotor1
            index = ord(text[i]) % 65
            charOne = self.rotor1[index]
            #print("Character " + text[i] + " maps to: " + charOne)


            ## Find the character routing from the index of self.rotor1[i]
            ## So input to second rotor will be the output from the first rotor
            index = ord(charOne) % 65
            charTwo = self.rotor2[index]
            #print("Character " + charOne + " maps to: " + charTwo)

            index = ord(charTwo) % 65
            charThree = self.rotor3[index]
            #print("Character " + charTwo + " maps to: " + charThree)

            ## Right before the reflector. So we've gone through R1, R2, R3

            ## Go back through rotor3
            index = self.reflector.find(charThree)
            charFour = chr(index + 65)
            #print("Reflector maps " + charThree + " to: " + charFour)

            ## Go back through rotor2
            index = self.rotor3.find(charFour)
            charFive = chr(index + 65)
            #print("Character " + charFour + " maps to: " + charFive)

            ## Go back through rotor1
            index = self.rotor2.find(charFive)
            charSix = chr(index + 65)
            #print("Character " + charFive + " maps to: " + charSix)

            index = self.rotor1.find(charSix)
            charSeven = chr(index + 65)
            #print("Character " + charSix + " maps to: " + charSeven)
            
            returnString += charSeven
        return returnString


ROTOR_I =   "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II =  "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
## A comes out of R3 then goes to the reflector
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
## Reflector returns Y
## Y = 25
## Find position 25 in R3. Thats R3s output


ROTOR_IV = "IMETCGFRAYSQBZXWLHKDVUPOJN"

ROTOR_TEST1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR_TEST2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR_TEST3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def main():

    ## Need two engima machines to both enrypt and decrypt at the same time
    engimaMachineINPUT = enigma(ROTOR_I, ROTOR_II, ROTOR_III, REFLECTOR_B, 0, 0, 0)
    engimaMachineOUTPUT = enigma(ROTOR_I, ROTOR_II, ROTOR_III, REFLECTOR_B, 0, 0, 0)

    inputText = input("Enter message: ")
    outputText = engimaMachineINPUT.encrypt(inputText)
    originalMessage = engimaMachineOUTPUT.encrypt(outputText)

    print("Original Message: " + originalMessage)
    print("Encrypted Message: " + outputText)

main()
