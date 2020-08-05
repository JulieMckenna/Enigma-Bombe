# Enigma-Bombe 

## Context
Our project was to create a simulated Enigma machine as well as Bombe machine. These two machines were based on the ones used in World War 2. The Enigma was used by the Germans to encode its messages, while the Bombe was used by the Allied Forces to “crack” the Enigma and decode the messages. An Enigma machine is quite complicated, it has 3 main components, a plugboard, rotors, and a reflector. We simulated an Enigma machine in python that would represent the physical electromechanical machine, as well as created a GUI that the user could interact with that looking similarly to what the physical machine looked like. After completing the Enigma portion, we moved on to Bombe which is a much more complicated machine. Bombe is basically multiple Enigma machines working at the same time to find the settings and decode a message. With the Bombe there is a crib, which is what the decoded message should equal. During World War 2, all the messages that were sent by the Germans started and ended the same way, this allowed the Bombe to work more effectively. Instead of guessing at what the whole message could mean, the crib only checked those phrases that were known to be there. The steps of Bombe are to take the encrypted message, run it through an Enigma machine (vary the settings each time), and then check if that output equaled the crib. If the decrypted message equaled the crib then the settings have been found and the rest of the message can be decoded, otherwise it keeps looking for the correct settings. These two machines worked to encode and decode messages during the War and can still be used today to encrypt messages. 

## Tutorial:
### Step by step guide:
  https://github.com/JulieMckenna/Enigma-Bombe/blob/master/UserGuide.txt

### Video Tutorials:
-Engima https://youtu.be/4P57gY-H6rU
-Bombe https://youtu.be/akjj7EOkeg4


## Setup and User Guide
Will be using Python and creating a user interface for people to encrypt and decrypt messages as they would like.

To use this: 
- Download the code (Clone this repo)
- Use Main.py to run the GUI - settings are set by the user through the GUI
- The GUI includes both the Enigma machine and Bombe machine
- GUI uses enigma.py to run an Enigma machine
- GUI uses bombe.py to run a Bombe machine - Bombe machine operates with given information (Rotor configuration is known, solves for offsets)
  - To use this it will ask for the users message - which in plain text - it will encode it to unkown settings (This is to ensure that the message being inputted to the bombe 
  was once put through an Enigma - make sure the settings can be found). It will concatenate the inputted string with HELLOWORLD - which will be used to crack the settings 
  since it will be used as a crib.
    - if the user if inputting an already encoded message without these steps - make sure that the encoded message has plain text of the messgae has helloworld at the end of it
    before encoding it to ensure that the bombe will work.
  - It will then ask to input the encrypted message and will print out the settings that machine was set to and the decrypted message.

## Enigma:
Required Parts - a plugboard (allows up to 10 letters to be swapped), 3 rotors (offset the alphabet), a reflector (the final step)
User input: Date of message (can be used to get the configuration from a database), 10 letter swaps, the 3 rotors(I - V), the reflector (A or B), and the message.
- There is an option that the user can check to show steps of the encryption

### Steps of encryption:
1. Swap plugboard connections
2. Go through rotors (1 -> 2 -> 3)
3. Go to reflector
4. Go back through rotors (3 -> 2 -> 1)
5. Plugboard swaps letters back
6. Print out final (encrypted) message

### Enigma Database:
- Will keep track of the engima settings for that day. 
- There is a schedule of enigma configurations for 10 different days in the database
#### Fields in the database: 
- There are fields for the 10 plugboard switches:
  - The characters going into the plugboard are stored in the db column 'PlugIn' as a 10 character string
  - The characters going out of the plugboard are stored in the db column 'PlugOut' as a 10 character string
  - These strings are prog
- The 3 rotors (int)
- The offsets for the 3 rotors (int)
- The reflector (char)

## Bombe:
- This is a very complicated machine. We had to simplify it down or else it would have taken too long to do
- To start all the encrypted messages need to have helloworld at the end of then ("messagehelloworld" -> then encrypt that)
  - This is needed for when the machine is checking the crib - if the last 10 letters of the decrptyed message = helloworld 
    means the settings have been found.
- The machine needs to go through and check all of the settings until the correct ones are found
- What we did to simplify it:
  - Used 3 rotors
  - The 3 rotors are known(i.e using Rotor I, Rotor II, and Rotor III, etc.)
  - There is no Plug board
    - adding this in required a lot more checking that needed to be done
   - The only thing the program needs to find is the offset of all three rotors

### Steps:
1. Give the Bombe the encrypted message(helloworld is the last 10 letters)
2. Bombe runs through a loop to create an Enigma machine with varried settings
3. Uses that machine to decrypt the message
4. If the last 10 letters of the decrypted message = helloworld
  a. The settings have been found and prints the decrypted messgae
  b. deletes that instance of the Enigma machine and repeats those steps with different setttings until the settings are found

### Bombe Database:
- Will log the correct configurations from the enigma machine that it is trying to emulate
- The table containing the discovered Enigma configurations is virtually identical to that of the Enigma machine itself, except:
  1. There is no plugboard
  2. Instead of saving the configurations by "Day" as the primary key, they are given a config ID
  3. The decrypted message that was used to crack the Enigma configuration is stored as well.

## GUI
The package we used for our GUI was TkInter. TkInter is the default GUI package that comes with Python. There are many functions that come along with the package, the functions we used are:

###
•	Label() – displays text or image anywhere in the window

•	Button() – displays a pushable block with text. When pressed, performs a certain function

•	Scale() – displays a slider with a range of values

•	OptionMenu() – displays a block that when pressed reveals a dropdown menu with multiple options

•	Entry() – Creates a text box on the window that users can enter values into

<img src="https://github.com/JulieMckenna/Enigma-Bombe/blob/master/gui%20enigma%20labels.png" width="750" height="650" />
Legend:

R1-R3: Rotor 1-3

Off1-Off3: Offset of rotor 1-3

p1-p10: Plugboard pair 1-10


### The GUI is split into two windows: Enigma and Bombe

#### Enigma:
  The enigma portion of the GUI uses all the functions stated above. The labels are used to define the various parts of the enigma machine, like defining the contents of an entry box or labeling a rotor. Users can interact with the buttons by simply pressing it. For example, if the button ‘H’ is pressed, the program will perform the function that is triggered by pressing ‘H’. In this case, the function is called CharcterClick(“H”), Which passes in ‘H’ as a parameter. Scale is used primarily to set the offset of our rotors in the enigma machine. OptionMenu is used for two things: to select a day to retrieve settings for that day or to choose which rotors are operating. Clicking “Choose a Day” will reveal a drop-down menu of the days that are available for selection (only 10 days). Pressing a rotor will display the 5 rotors that are available to use. The entry boxes are dependent on the actions of a button. When a character is pressed, the normal character and encrypted character are display in their respective entry boxes. If the user is typing a message into an entry field, a button should be linked to the entry box to retrieve the message and perform the desired function.
#### Bombe:
  The Bombe window can only be accessed by pressing the button ‘Go to Bombe Window’ on the enigma terminal. This window is much simpler than the enigma window. When the user enters the encrypted message, pressing the button “Run Encryption” will retrieve the message from the entry box and pass it into the Bombe machine
