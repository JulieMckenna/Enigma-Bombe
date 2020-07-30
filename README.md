# Enigma-Bombe Context
Our project was to create a simulated Enigma machine as well as Bombe machine. These two machines were based on the ones used in World War 2. The Enigma was used by the Germans to encode its messages, while the Bombe was used by the Allied Forces to “crack” the Enigma and decode the messages. An Enigma machine is quite complicated, it has 3 main components, a plugboard, rotors, and a reflector. We simulated an Enigma machine in python that would represent the physical electromechanical machine, as well as created a GUI that the user could interact with that looking similarly to what the physical machine looked like. After completing the Enigma portion, we moved on to Bombe which is a much more complicated machine. Bombe is basically multiple Enigma machines working at the same time to find the settings and decode a message. With the Bombe there is a crib, which is what the decoded message should equal. During World War 2, all the messages that were sent by the Germans started and ended the same way, this allowed the Bombe to work more effectively. Instead of guessing at what the whole message could mean, the crib only checked those phrases that were known to be there. The steps of Bombe are to take the encrypted message, run it through an Enigma machine (vary the settings each time), and then check if that output equaled the crib. If the decrypted message equaled the crib then the settings have been found and the rest of the message can be decoded, otherwise it keeps looking for the correct settings. These two machines worked together to encode and decode messages during the War and can still be used today to encrypt messages. 



# Setup and User Guide
Will be using Python and creating a user interface for people to encrypt and decrypt messages as they would like.

To use this: 
- Download the code(Clone this repo)
- Run CreateDB.py to create the database (Need to fix this file or delete this sectiion)
- Use Main.py to run the GUI - settings are set by the user through the GUI
- The GUI includes both the Enigma machine and Bombe machine
- GUI uses enigma.py to run an Enigma machine - settings are set in the main loop at the bottom
- GUI uses bombe.py to run a Bombe machine - This ended up using a less complicated enigma machine
  - To use this it will ask for the users message - which in plain text - it will encode it to unkown settings(This is to ensure that the message being inputted to the bombe 
  was once put through an Enigma - make sure the settings can be found). It will concatenate the inputted string with HelloWorld - which will be used to crack the settings 
  since it will be used as a crib.
    - if the user if inputting an already encoded message without these steps - make sure that the encoded message has plain text of the messgae has helloworld at the end of it
    before encoding it to ensure that the bombe will work.
  - It will then ask to input the encrypted message and will print out the settings that machine was set to and the decrypted message.

# Enigma:
Required Parts - a plugboard(allows up to 10 letters to be swapped), 3 rotors(offset the alphabet), a reflector(the final step)
User input: Date of message(can be used to auto fill the variables from a database), 10 letter swaps, the 3 rotors(I - V), the reflector (A or B), and the message.
- There is an option that the user can check to show steps of the encryption

### Steps of encryption:
1. Swap plugboard connections
2. Go through rotors (1 -> 2 -> 3)
3. Go to reflector
4. Go back through rotors (3 -> 2 -> 1)
5. Swap letters back 
6. Print out final(encrypted) message

### Enigma Database:
- Will keep track of the engima settings for that day. 
- A schedule can be created by importing from an excel file, and loading in the GUI, or by creating your own configuration in the GUI

#### Fields in the database: 
- There are fields for the 10 plugboard switches:
  - The characters going into the plugboard are stored in the db column 'PlugIn' as a 10 character string
  - The characters going out of the plugboard are stored in the db column 'PlugOut' as a 10 character string
  - These strings are prog
- The 3 rotors (int)
- The offsets for the 3 rotors (int)
- The reflector

# Bombe:
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

#### Steps:
1. Give the Bombe the encrypted message(helloworld is the last 10 letters)
2. Bombe runs through a loop to create an Enigma machine with varried settings
3. Uses that machine to decrypt the message
4. If the last 10 letters of the decrypted message = helloworld
  a. The settings have been found and prints the decrypted messgae
  b. deletes that instance of the Enigma machine and repeats those steps with different setttings until the settings are found

### Bombe Database:
- Will hold the correct settings the enigma machine
- The PossibleConfigs table will log all configurations that the Bombe machine iterates through
- When the correct configuration is found, the correct configuration is inserted into KnownConfigs,and the rest of the configurations for that particular day is that are incorrect will be deleted from the PossibleConfigs table.

### Tutorial:
-Engima https://youtu.be/4P57gY-H6rU
-Bombe https://youtu.be/akjj7EOkeg4
