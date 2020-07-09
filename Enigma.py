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

def printalphabet(num):
    for x in range(26):
        print(alphabet[num,x])

def plugboard(ogletter, swapedletter):
    print("Plugboard section")
    print("Swapping letter: " + ogletter + " with: " + swapedletter)
    #swap the letters
    ogletterindex = 0
    swapletterindex = 0
    #search for the index of letters to swap
    for x in range(26):
        if (alphabet[1, x] == ogletter):
            ogletterindex = x
            #print(str(ogletterindex))
        if (alphabet[1, x] == swapedletter):
            swapletterindex = x
    #swap the two in the array
    alphabet[1, ogletterindex] = swapedletter
    alphabet[1, swapletterindex] = ogletter
    #prints cipher alphabet to check that the swap worked
    #printalphabet(1)
#letter can not ve encoded as its self so swaps letters that are encoded as themselves
def reflector(reflectortype):
    #reflector a - will go through cipher array and if the letter is the same as its orignal will swap it
    if reflectortype == "A":
        swap = [0]*26
        reflectionvalid = False
        #gets all the letters that are encoded as themselves
        while(reflectionvalid == False):
            reflectionvalid = True
            for i in range(26):
                if alphabet[1,i] == alphabet[0,i]:
                    reflectionvalid = False
                    #print("letter is the same as plain text letter" + alphabet[0,i])
                    swap[i] = 1
            print(swap)
            #works if divisible by 2
            for i in range(26):
                #if encoded as its self
                if swap[i] == 1:
                    #find next instance that is encoded as itself
                    if i < 26:
                        for r in range((i+1),26):
                            if swap[r] == 1:
                                letterswap(1, i, r)
                                swap[i] = 0
                                swap[r] = 0            

def letterswap(alpha,index1,index2):
    templetter = alphabet[alpha,index1]
    alphabet[alpha,index1] = alphabet[alpha,index2]
    alphabet[alpha,index2] = templetter

def removespaces(str):
    return str.replace(" ", "")

#menu
#get input message
plainTextMessage = input("What is the message you would like to input\t").upper()
#get rid of spaces
plainTextMessage = removespaces(plainTextMessage)
print(plainTextMessage)


#get settings 
#plug board
for x in range(3):
    print("Plugboard connection: " + str(x) + "/10")
    OrigLetter = input("What letter would you like to swap?\t").upper()
    ChangeLetter = input("What is it being changed to?\t").upper()
    plugboard(OrigLetter, ChangeLetter)
#prints cipher alphabet after all the changes are made
#printalphabet(1)

#rotors
#goes through 1, 2, 3 - thne reflector - thne back 3, 2, 1
"""
rotorarray = []
for x in range(3):
    rotornum = input("What is the rotor you would like to use?")
    rotorarray.append(rotornum)
#prints cipher alphabet after all the changes are made
printalphabet(1)
"""

#reflector
reflectortype = input("Please choose the reflector(A or B):\t")
reflector(reflectortype)


print("The encoded message is: ")
ciphertext = ""
#do the transformation from plain to cipher
for x in range(len(plainTextMessage)):
    templetter = plainTextMessage[x]
    #print(alphabet[0,x])
    for i in range(26):
        #print(alphabet[0,x])
        if templetter == alphabet[0,i]:
            changeletter = alphabet[1,i]
    ciphertext += changeletter
print(ciphertext)




