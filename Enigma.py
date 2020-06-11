#Enigma code

#array for the a

#menu
#get input message
plainTestMessage = input("What is the message you would like to input")
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
