from tkinter import *
from tkinter import messagebox

from enigma import *
from bombegui import *
import DatabaseFunctions
import time
edb = DatabaseFunctions.EnigmaDatabase()
root = Tk()

root['background']= '#9C9C9C'
def closeEvent(edb):
    #print("DB is gon gon")
    del edb
root.protocol("WM_DELETE_WINDOW",closeEvent(edb))
root.title("Enigma")

#adding image to window
frame = 0
def gif():
    while True:
        try:
            global photo
            global frame
            global label
            photo = PhotoImage(file = "enigma.gif", format = "gif - {}".format(frame))
            label.configure(image = photo)
            frame = frame + 1
            break
        except Exception:
            frame = 1
            break
def setBlank():
    global label
    global frame
    while frame <22:
        time.sleep(.2)
        root.after(500, lambda: gif())
        label.update()
photo = PhotoImage(file = "enigma.gif",)
label = Label(image = photo,highlightcolor="black")
label.grid(row = 0, column = 0, columnspan = 6, sticky= W+N)
animate = Button(root, text = "animate",bg= "#D0D0D0" ,command = setBlank)
animate.grid(row= 1, column = 2,columnspan=2,sticky = N)
#labeling rotors

labelr3 = Label(root,text="R3",background="#9C9C9C" )
labelr3.grid(row=0,column=6,sticky=S)

labelr2 = Label(root,text="R2",background="#9C9C9C")
labelr2.grid(row=0,column=8,sticky=S)

labelr1 = Label(root,text="R1",background="#9C9C9C")
labelr1.grid(row=0,column=10,sticky=S)

labeloff3 = Label(root,text="Off3",background="#9C9C9C")
labeloff3.grid(row=0,column=6,sticky=N+E)

labeloff2 = Label(root,text="Off2",background="#9C9C9C")
labeloff2.grid(row=0,column=8,sticky=N+E)

labeloff1 = Label(root,text="Off1",background="#9C9C9C")
labeloff1.grid(row=0,column=10,sticky=N+E)

# rotor position sliders and displaying on screen
off1 = pRotor1 = Scale(root, from_=1, to=26, highlightbackground = "black",background = "black",fg = "White")
pRotor1.grid(row=0, column=6)
off2 = pRotor2 = Scale(root, from_=1, to=26, highlightbackground = "black",background = "black",fg = "White")
pRotor2.grid(row=0, column=8)
off3 = pRotor3 = Scale(root, from_=1, to=26, highlightbackground = "black",background = "black",fg = "White")
pRotor3.grid(row=0, column=10)
# rotor selection
showHide = IntVar()
def1 = StringVar(root)
def2 = StringVar(root)
def3 = StringVar(root)
choices = {'1', '2', '3', '4', '5'}
rotors = [3, 2, 1]
def1.set('3')
def2.set('2')
def3.set('1')
rotorFlag = 0
def rotorTest(*args):
    args=args[0].strip("PY_VAR")
    args = int(args)
    if args == 1:
        rotors[0] = int(def1.get())
    elif args == 2:
        rotors[1] = int(def2.get())
    else:
        rotors[2] = int(def3.get())
#   print(rotors)
    if rotors[0] == rotors[1]:
        rW.delete(0, END)
        rW.insert(0, "Each rotor must be unique")
        global rotorFlag
        rotorFlag = 1
    elif rotors[0] == rotors[2]:
        rW.delete(0, END)
        rW.insert(0, "Each rotor must be unique")
        rotorFlag = 1
    elif rotors[1] == rotors[2]:
        rW.delete(0, END)
        rW.insert(0, "Each rotor must be unique")
        rotorFlag = 1
    else:
        rW.delete(0, END)
        rotorFlag = 0
    print(rotors)
e1c = Checkbutton(root, text="Show Encryption Steps In Terminal", variable=showHide,bg="#9C9C9C",highlightbackground="#9C9C9C")
e1c.grid(row=10, column=0, columnspan=18)
dropDown1 = OptionMenu(root, def1, *choices)    #Dropdown menu for rotor selection
dropDown1.grid(row=1, column=6)                 #
dropDown2 = OptionMenu(root, def2, *choices)    #
dropDown2.grid(row=1, column=8)                 #
dropDown3 = OptionMenu(root, def3, *choices)    #
dropDown3.grid(row=1, column=10)                #
def1.trace("w", rotorTest)
def2.trace("w", rotorTest)
def3.trace("w", rotorTest)

rW = Entry(root, width=30, borderwidth=5,highlightcolor = "#000000")
rW.grid(row=1, column=14, columnspan=6)
# cypher keyboard
# toprow
cQ = Button(root, text="Q", padx=10, pady=10,bg="black",fg="White")
cQ.grid(row=2, column=0)
cW = Button(root, text="W", padx=10, pady=10,bg="black",fg="White")
cW.grid(row=2, column=2)
cE = Button(root, text="E", padx=10, pady=10,bg="black",fg="White")
cE.grid(row=2, column=4)
cR = Button(root, text="R", padx=10, pady=10,bg="black",fg="White")
cR.grid(row=2, column=6)
cT = Button(root, text="T", padx=10, pady=10,bg="black",fg="White")
cT.grid(row=2, column=8)
cY = Button(root, text="Y", padx=10, pady=10,bg="black",fg="White")
cY.grid(row=2, column=10)
cU = Button(root, text="U", padx=10, pady=10,bg="black",fg="White")
cU.grid(row=2, column=12)
cI = Button(root, text="I", padx=10, pady=10,bg="black",fg="White")
cI.grid(row=2, column=14)
cO = Button(root, text="O", padx=10, pady=10,bg="black",fg="White")
cO.grid(row=2, column=16)
cP = Button(root, text="P", padx=10, pady=10,bg="black",fg="White")
cP.grid(row=2, column=18)
# middlerow
cA = Button(root, text="A", padx=10, pady=10,bg="black",fg="White")
cA.grid(row=3, column=1)
cS = Button(root, text="S", padx=10, pady=10,bg="black",fg="White")
cS.grid(row=3, column=3)
cD = Button(root, text="D", padx=10, pady=10,bg="black",fg="White")
cD.grid(row=3, column=5)
cF = Button(root, text="F", padx=10, pady=10,bg="black",fg="White")
cF.grid(row=3, column=7)
cG = Button(root, text="G", padx=10, pady=10,bg="black",fg="White")
cG.grid(row=3, column=9)
cH = Button(root, text="H", padx=10, pady=10,bg="black",fg="White")
cH.grid(row=3, column=11)
cJ = Button(root, text="J", padx=10, pady=10,bg="black",fg="White")
cJ.grid(row=3, column=13)
cK = Button(root, text="K", padx=10, pady=10,bg="black",fg="White")
cK.grid(row=3, column=15)
cL = Button(root, text="L", padx=10, pady=10,bg="black",fg="White")
cL.grid(row=3, column=17)
# lowerrow
cZ = Button(root, text="Z", padx=10, pady=10,bg="black",fg="White")
cZ.grid(row=4, column=2)
cX = Button(root, text="X", padx=10, pady=10,bg="black",fg="White")
cX.grid(row=4, column=4)
cC = Button(root, text="C", padx=10, pady=10,bg="black",fg="White")
cC.grid(row=4, column=6)
cV = Button(root, text="V", padx=10, pady=10,bg="black",fg="White")
cV.grid(row=4, column=8)
cB = Button(root, text="B", padx=10, pady=10,bg="black",fg="White")
cB.grid(row=4, column=10)
cN = Button(root, text="N", padx=10, pady=10,bg="black",fg="White")
cN.grid(row=4, column=12)
cM = Button(root, text="M", padx=10, pady=10,bg="black",fg="White")
cM.grid(row=4, column=14)
#space between 1st and second key
srow4 = Label(root,bg = "#575757",bd=0,highlightbackground="Black",text="                                                                                                                                                                                                                                                                                                                                          ")

srow4.grid(row=5,column=0,columnspan=30)

#normal keyboard
#top row
nQ = Button(root, text="Q", padx=10, pady=10,relief=RIDGE ,command = lambda: charClick("Q"))
nQ.grid(row=6, column=0)
nW = Button(root, text="W", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("W"))
nW.grid(row=6, column=2)
nE = Button(root, text="E", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("E"))
nE.grid(row=6, column=4)
nR = Button(root, text="R", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("R"))
nR.grid(row=6, column=6)
nT = Button(root, text="T", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("T"))
nT.grid(row=6, column=8)
nY = Button(root, text="Y", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("Y"))
nY.grid(row=6, column=10)
nU = Button(root, text="U", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("U"))
nU.grid(row=6, column=12)
nI = Button(root, text="I", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("I"))
nI.grid(row=6, column=14)
nO = Button(root, text="O", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("O"))
nO.grid(row=6, column=16)
nP = Button(root, text="P", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("P"))
nP.grid(row=6, column=18)
#middlerow
nA = Button(root, text="A", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("A"))
nA.grid(row=7, column=1)
nS = Button(root, text="S", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("S"))
nS.grid(row=7, column=3)
nD = Button(root, text="D", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("D"))
nD.grid(row=7, column=5)
nF = Button(root, text="F", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("F"))
nF.grid(row=7, column=7)
nG = Button(root, text="G", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("G"))
nG.grid(row=7, column=9)
nH = Button(root, text="H", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("H"))
nH.grid(row=7, column=11)
nJ = Button(root, text="J", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("J"))
nJ.grid(row=7, column=13)
nK = Button(root, text="K", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("K"))
nK.grid(row=7, column=15)
nL = Button(root, text="L", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("L"))
nL.grid(row=7, column=17)
#bottomrow
nZ = Button(root, text="Z", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("Z"))
nZ.grid(row=8, column=2)
nX = Button(root, text="X", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("X"))
nX.grid(row=8, column=4)
nC = Button(root, text="C", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("C"))
nC.grid(row=8, column=6)
nV = Button(root, text="V", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("V"))
nV.grid(row=8, column=8)
nB = Button(root, text="B", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("B"))
nB.grid(row=8, column=10)
nN = Button(root, text="N", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("N"))
nN.grid(row=8, column=12)
nM = Button(root, text="M", padx=10, pady=10,relief=RIDGE, command = lambda: charClick("M"))
nM.grid(row=8, column=14)
#space between keyboards
srow8 = Label(root,bg = "#575757",pady=0,text="                                                                                                                                                                                                                                                                                                                                        ")
srow8.grid(row=9,column=0,columnspan=30)

#Encryption button
eB = Button(root, text="Run Encryption", padx=2, pady=2,bg= "#D0D0D0" , command = lambda: charClick("AA"))
eB.grid(row=12, column=14, columnspan=3)

pB = Button(root, text="Apply Plugboard", padx=2, pady=2,bg= "#D0D0D0" ,command = lambda: applyplug())
pB.grid(row=16, column=14, columnspan=3)

#textboxes
clabel = Label(root,text="Encrypted Message",bg="#9C9C9C")
clabel.grid(row=11,column=0,columnspan=18)

ctext = Entry(root,width=50,borderwidth=3,background="Black",fg="White",font =7)
ctext.grid(row=12,column=0,columnspan=18)

nlabel = Label(root,text="Normal Message",bg="#9C9C9C")
nlabel.grid(row=13,column=0,columnspan=18)

ntext = Entry(root,width=50,borderwidth=3,font=7)
ntext.grid(row=14,column=0,columnspan=18)

plabel = Label(root, text="Plugboard Pairs",bg="#9C9C9C")
plabel.grid(row=15,column=0,columnspan=18)

ptext = Entry(root,width=50, borderwidth=3,fg = "#373737")
ptext.grid(row=16,column=0,columnspan=18)
counter = 0
charOut = 'a'
letters = [cA, cB, cC, cD, cE, cF, cG, cH, cI, cJ, cK, cL, cM, cN, cO, cP, cQ, cR, cS, cT, cU, cV, cW, cX, cY, cZ]
global settings


def applyplug():
    global settings
    settings = ptext.get()
    print(settings)
    return



def incrementCounter():
    global counter
    counter +=1
def lightLetter(letter):
    letterIndex = ord(letter) % 65
    letters[letterIndex].configure(bg = "Yellow", fg = "Black")
    root.after(1000, lambda: letters[letterIndex].configure(bg="Black", fg="White"))
def charClick(abc):     #still need to make
    if rotorFlag == 1:
        print("Make sure your rotors are valid")
        return
    show = int(showHide.get())
    single = len(abc)
    #print(abc)
    global rotorPass
    rotorPass = ["","",""]
    for i in range(3):
        if rotors[i] == 1:
            rotorPass[i] = ROTOR_I
        elif rotors[i] == 2:
            rotorPass[i] = ROTOR_II
        elif rotors[i] == 3:
            rotorPass[i] = ROTOR_III
        elif rotors[i] == 4:
            rotorPass[i] = ROTOR_IV
        elif rotors[i] == 5:
            rotorPass[i] = ROTOR_V

        #print(rotorPass[i])
    #print(off1.get()-1+counter)
    if single == 1:
        if counter == 0:
            global charOut
            applyplug()
            if show == 1:
                charOut = enigma(settings, [], rotorPass[2], rotorPass[1], rotorPass[0], REFLECTOR_B, off3.get()-1, off2.get()-1, off1.get()-1, True)
            else:
                charOut = enigma(settings, [], rotorPass[2], rotorPass[1], rotorPass[0], REFLECTOR_B, off3.get()-1, off2.get() - 1, off1.get() - 1, False)
            #print("input", abc)
            letter=charOut.encrypt(abc)
            lightLetter(letter)
            current = ctext.get()
            ctext.delete(0, END)
            ctext.insert(0, str(current) + str(letter))
            normal = ntext.get()
            ntext.delete(0, END)
            ntext.insert(0, str(normal) + str(abc))
            #print(letter)
        else:
            letter = charOut.encrypt(abc)
            lightLetter(letter)
            current = ctext.get()
            ctext.delete(0, END)
            ctext.insert(0, str(current) + str(letter))
            normal = ntext.get()
            ntext.delete(0, END)
            ntext.insert(0, str(normal) + str(abc))
            #print(letter)
        #print(counter)
        incrementCounter()
    else:
        normaltext = ntext.get()
        if(normaltext.isupper() == False):
            message = "Your Entry must be all CAPS!"
            messagebox.showinfo("Syntax Error", message)
            ntext.delete(0, END)
            return
        elif((" " in normaltext) == True):
            message = "Entry should contain no spaces!"
            messagebox.showinfo("Syntax Error", message)
            ntext.delete(0, END)
            return
        else:
            pass

        applyplug()
        if show == 1:
            charOut2 = enigma(settings, [], rotorPass[2], rotorPass[1], rotorPass[0], REFLECTOR_B, off3.get() - 1, off2.get() - 1, off1.get() - 1, True)
        else:
            charOut2 = enigma(settings, [], rotorPass[2], rotorPass[1], rotorPass[0], REFLECTOR_B, off3.get() - 1, off2.get() - 1, off1.get() - 1, False)
        # print("input", abc)
        letter = charOut2.encrypt(ntext.get())
        current = ctext.get()
        ctext.delete(0, END)
        ctext.insert(0, str(current) + str(letter))
        # print(letter)
# Section for Bombe
bombebutton = Button(root,text="Go to Bombe Window",bg = "#CB6F00",command = lambda: bombewindow())
bombebutton.grid(row=14,column=0,columnspan = 4)
def bombewindow():
    secondwindow = Toplevel()#creating second window
    secondwindow['background'] = '#D87600'
    secondwindow.title("Bombe")
    cLabel = Label(secondwindow,text="Enter the encrypted message into Bombe",bg = "#D87600")
    cLabel.grid(row=0,column=0)
    global cMessage
    cMessage = Entry(secondwindow, width=50, borderwidth=3,font=7,background="Black",fg="White")
    cMessage.grid(row=1,column=0)
    decryptb = Button(secondwindow,text = "Run decryption",bg= "#D0D0D0",command = lambda: callbombe())
    decryptb.grid(row=1,column=1)
    space1 = Label(secondwindow, text="                   ",bg = "#D87600")
    space1.grid(row=2, column=0)
    combination = Label(secondwindow, text="The combination of rotors found",bg = "#D87600")
    combination.grid(row=3, column=0)
    numtries = Label(secondwindow, text="Combinations Tried:",bg = "#D87600")
    numtries.grid(row=3, column=1)
    global ncombination
    ncombination = Entry(secondwindow, width=50, borderwidth=3)
    ncombination.grid(row=4, column=0)
    global tries
    tries = Entry(secondwindow, width=10, borderwidth=3)
    tries.grid(row=4, column=1)
    space2 = Label(secondwindow, text="                   ",bg = "#D87600")
    space2.grid(row=5, column=0)
    nLabel = Label(secondwindow, text="Decrypted message",bg = "#D87600")
    nLabel.grid(row=6, column=0)
    global decryptm
    decryptm = Entry(secondwindow, width=50, borderwidth=3,font=7)
    decryptm.grid(row=7, column=0)
def setcombo(s):
    ncombination.delete(0, END)
    ncombination.insert(0, s)
def setdecrpt(m):
    decryptm.delete(0, END)
    decryptm.insert(0, m)
def setattempts(a):
    tries.delete(0,END)
    tries.insert(0,a)
def callbombe():
    mess = cMessage.get()
    #print(mess)
    bombe3(mess, rotorPass[2], rotorPass[1], rotorPass[0])#calling from bombegui.py
    if(getstatus() == False):
        message = "Bombe was unable to find settings\n Make sure plugboard is empty and message from enigma has 'HELLOWORLD' at the end of message"
        messagebox.showinfo("Bombe Error", message)
        return
    else:
        pass
    s = retrivesettings()
    m = retrivemessage()
    a = gettries()
    setcombo(s)
    setdecrpt(m)
    setattempts(a)

#Day selection from database
options = [1,2,3,4,5,6,7,8,9,10]
var = StringVar()
var.set("Choose a Day")

day = OptionMenu(root,var,*options)
day.grid(row=0,column=11,columnspan=3,sticky=N)

labelday = Label(root,text="(Day,'p1,p2,p3,p4,p5,p6,p7,p7,p9,p10',r1,off1,r2,off2,r3,off3,n/a",bg="#9C9C9C",fg="#FFFFFF")
labelday.grid(row=0,column=14,columnspan=21,stick=N)

daye = Entry(root,width=50,borderwidth=5,fg = "#373737")
daye.grid(row=0,column= 14,columnspan=21 )

chooseday = Button(root,text="Confirm Day",bg= "#D0D0D0" ,command = lambda:insertday())
chooseday.grid(row=0,column=11,columnspan=3)

pluglabel = Label(root,text="p1,p2,p3,p4,p5,p6,p7,p8,p9,p10",bg = "#9C9C9C")
pluglabel.grid(row=20,column=4,columnspan=10)

def insertday():
    en = daye.get()
    selection = var.get()
    iselection = int(selection)
    dayfinal= edb.getConfiguration(iselection)
    sdayfinal = str(dayfinal)
    daye.delete(0, END)
    daye.insert(0,sdayfinal)



mainloop()