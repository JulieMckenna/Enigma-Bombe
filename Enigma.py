#Enigma code

import array

#array for the alphabet
alphabet = {(i,j): 0 for i in range(2) for j in range(26)}

#to get the upper case letter corresponding to each num of the alphabet
charnum = 65
for x in range(26):
    alphabet[0, int(x)] = chr(charnum)
    alphabet[1, int(x)] = chr(charnum)
    charnum+=1
for x in range(26):
    print(alphabet[0,x])
    print(alphabet[1,x])

#menu
#get input message
plainTestMessage = input("What is the message you would like to input")
#get rid of spaces
#make uppercase so chars match with the alphabet

#get settings 
#plug board
for x in range(10):
    print("Plugboard connection: " + x + "/10")
    OrigLetter = input("What letter would you like to swap?")
    ChangeLetter = input("What is it being changed to?")
#rotors
rotorarray = []
for x in range(3):
    rotornum = input("What is the " + x + " you would like to use?")
    rotorarray.append(rotornum)
#reflector
reflector = input("Please choose the reflector")

print("The encoded message is: ")

def plugboard(ogletter, swapedletter):
    print("Plugboard section")
    print("Swapping letter: " + ogletter + " with: " + swapedletter)
    #swap the letters

    #search for where the ogletter is (index)

    #serach for where the swapped letter (index)

    #swap the two in the array

