################## NOTES #################

## 1. Need to figure out the rotor offset. index = ord(text[i + self.r1]) % 65 ????



class rotors:
    rotor1 = ""
    rotor2 = ""
    rotor3 = ""

    def __init__(self, rotor1, rotor2, rotor3, offset1, offset2, offset3):
        
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3

        ## Setup the rotor with the offset taken into account
        ## If the rotor was "ABCD" with an offset of 2, the new rotor would be "DCAB"
        ## So, the rotor of "ABCD" starts at position 2 of the string, and is looped like a wheel/rotor

        for i in range(0, offset1):
            self.rotor1 = self.stepRotor(self.rotor1)

        for i in range(0, offset2):
            self.rotor2 = self.stepRotor(self.rotor2)

        for i in range(0, offset3):
            self.rotor3 = self.stepRotor(self.rotor3)


    ## Function to step rotor by 1 position
    ## Input is the rotor string
    ## Each char needs to move right by 1, and the last char needs to go into the first position
    def stepRotor(self, rotor):
        print("Stepping rotor by 1 place")
        ## Save last char
        lastChar = rotor[25]
        returnString = rotor[25]
        ## Move each char forward 1 position
        for i in range(0, len(rotor) - 1):
            rotorAsList = list(rotor)
            tempChar = rotorAsList[i]
            rotorAsList[i + 1] = tempChar
            returnString += rotorAsList[i + 1]
        print(returnString)
        return returnString

    def encrypt(self, text):
        
        ## Count for how many times each rotor is stepped. Don't care how many times rotor3 is stepped
        r1_count = 0
        r2_count = 0


        returnString = ""

        print("Rotor I: " + self.rotor1)
        print("Rotor II: " + self.rotor2)
        print("Rotor III: " + self.rotor3)
        print("Initial String: " + text)


        ## Loop through each character of the text provided
        for i in range(0, len(text)):
            ## Find the index of the current char CHAR % 65 should give index of an uppercase character
            ## ord(char) returns unicode of character in Python

            ## Find character routing from index of text[i]
            ## charOne is the output from rotor1
            index = ord(text[i]) % 65
            charOne = self.rotor1[index]
            print("Character " + text[i] + " maps to: " + charOne)


            ## Find the character routing from the index of self.rotor1[i]
            ## So input to second rotor will be the output from the first rotor
            index = ord(self.rotor1[index]) % 65
            charTwo = self.rotor2[index]
            print("Character " + charOne + " maps to: " + charTwo)

            index = ord(self.rotor2[index]) % 65
            charThree = self.rotor3[index]
            print("Character " + charTwo + " maps to: " + charThree)

            returnString += charThree

            ## Step rotor 1 every iteration
            self.rotor1 = self.stepRotor(self.rotor1)
            r1_count += 1

            ## Step rotor 2 if rotor 1 has been stepped 26 times
            if(r1_count == 25):
                self.rotor2 = self.stepRotor(self.rotor2)
                r1_count = 0
                r2_count += 1
            ## Step rotor 3 if rotor 2 has been stepped 26 times
            if(r2_count == 25):
                r2_count = 0
                self.rotor3 = self.stepRotor(self.rotor3)

            print(r1_count)
            print(r2_count)

        return returnString


ROTOR_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
ROTOR_IV = "IMETCGFRAYSQBZXWLHKDVUPOJN"

ROTOR_TEST1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR_TEST2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR_TEST3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rotorTest = rotors(ROTOR_TEST1, ROTOR_TEST2, ROTOR_TEST3, 0, 0, 0)
print(rotorTest.encrypt("AAAAA"))

## After one rotation, we need to shift the first rotor by 1 position
## So, if input = ["ABC"]
## And rotor1 = ["CBA"]
## then after 1 rotation, the rotor1 should be

## Ring settings set what index of the rotor array to start at
## Rotor setup is what characters are held at what indices of the rotor
## So, Rotor1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" could be a rotor in alphabetical order
## And the rotor setup could be r1 = 2. So the first inputted character is going to be encoded to be a C
## When that first letter goes through the reflector, it will come back as a D

## For the indices going through the rotor array, they need to be able to start at any value and then reset to 0 if they go past i = 25 for instance