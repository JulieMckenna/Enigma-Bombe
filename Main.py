from tkinter import *

root = Tk()
root.title("Enigma")
# root.geometry("400X400")
# rotor position sliders and displaying on screen
pRotor1 = Scale(root, from_=1, to=26)
pRotor1.grid(row=0, column=6)
pRotor2 = Scale(root, from_=1, to=26)
pRotor2.grid(row=0, column=8)
pRotor3 = Scale(root, from_=1, to=26)
pRotor3.grid(row=0, column=10)
# rotor selection
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
show = IntVar()
def1 = StringVar(root)
def2 = StringVar(root)
def3 = StringVar(root)
choices = {'1', '2', '3', '4', '5'}
rotors = [1, 2, 3]
def1.set('1')
def2.set('2')
def3.set('3')
def test(*args):
    args=args[0].strip("PY_VAR")
#    print(args)
    args = int(args)
    if args == 6:
        tempRotor=int(def1.get())
        rotors[0] = tempRotor
    elif args == 7:
        tempRotor=int(def2.get())
        rotors[1] = tempRotor
    else:
        tempRotor=int(def3.get())
        rotors[2] = tempRotor
#   print(rotors)
    if rotors[0] == rotors[1]:
        rW.delete(0, END)
        rW.insert(0, "Each rotor must be unique")
    elif rotors[0] == rotors[2]:
        rW.delete(0, END)
        rW.insert(0, "Each rotor must be unique")
    elif rotors[1] == rotors[2]:
        rW.delete(0, END)
        rW.insert(0, "Each rotor must be unique")
    else:
        rW.delete(0, END)
e1c = Checkbutton(root, text="Show Encryption Steps In Terminal", variable=show)
e1c.grid(row=10, column=0, columnspan=18)
dropDown1 = OptionMenu(root, def1, *choices)    #Dropdown menu for rotor selection
dropDown1.grid(row=1, column=6)                 #
dropDown2 = OptionMenu(root, def2, *choices)    #
dropDown2.grid(row=1, column=8)                 #
dropDown3 = OptionMenu(root, def3, *choices)    #
dropDown3.grid(row=1, column=10)                #
def1.trace("w", test)
def2.trace("w", test)
def3.trace("w", test)

rW = Entry(root, width=30, borderwidth=3)
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
c0 = Button(root, text="O", padx=10, pady=10,bg="black",fg="White")
c0.grid(row=2, column=16)
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
srow4 = Label(root,text="         ")
srow4.grid(row=5,column=0,columnspan=18)

#normal keyboard
#top row
nQ = Button(root, text="Q", padx=10, pady=10, command = lambda: charClick("Q"))
nQ.grid(row=6, column=0)
nW = Button(root, text="W", padx=10, pady=10, command = lambda: charClick("W"))
nW.grid(row=6, column=2)
nE = Button(root, text="E", padx=10, pady=10, command = lambda: charClick("E"))
nE.grid(row=6, column=4)
nR = Button(root, text="R", padx=10, pady=10, command = lambda: charClick("R"))
nR.grid(row=6, column=6)
nT = Button(root, text="T", padx=10, pady=10, command = lambda: charClick("T"))
nT.grid(row=6, column=8)
nY = Button(root, text="Y", padx=10, pady=10, command = lambda: charClick("Y"))
nY.grid(row=6, column=10)
nU = Button(root, text="U", padx=10, pady=10, command = lambda: charClick("U"))
nU.grid(row=6, column=12)
nI = Button(root, text="I", padx=10, pady=10, command = lambda: charClick("I"))
nI.grid(row=6, column=14)
n0 = Button(root, text="O", padx=10, pady=10, command = lambda: charClick("O"))
n0.grid(row=6, column=16)
nP = Button(root, text="P", padx=10, pady=10, command = lambda: charClick("P"))
nP.grid(row=6, column=18)
#middlerow
nA = Button(root, text="A", padx=10, pady=10, command = lambda: charClick("A"))
nA.grid(row=7, column=1)
nS = Button(root, text="S", padx=10, pady=10, command = lambda: charClick("S"))
nS.grid(row=7, column=3)
nD = Button(root, text="D", padx=10, pady=10, command = lambda: charClick("D"))
nD.grid(row=7, column=5)
nF = Button(root, text="F", padx=10, pady=10, command = lambda: charClick("F"))
nF.grid(row=7, column=7)
nG = Button(root, text="G", padx=10, pady=10, command = lambda: charClick("G"))
nG.grid(row=7, column=9)
nH = Button(root, text="H", padx=10, pady=10, command = lambda: charClick("H"))
nH.grid(row=7, column=11)
nJ = Button(root, text="J", padx=10, pady=10, command = lambda: charClick("J"))
nJ.grid(row=7, column=13)
nK = Button(root, text="K", padx=10, pady=10, command = lambda: charClick("K"))
nK.grid(row=7, column=15)
nL = Button(root, text="L", padx=10, pady=10, command = lambda: charClick("L"))
nL.grid(row=7, column=17)
#bottomrow
nZ = Button(root, text="Z", padx=10, pady=10, command = lambda: charClick("Z"))
nZ.grid(row=8, column=2)
nX = Button(root, text="X", padx=10, pady=10, command = lambda: charClick("X"))
nX.grid(row=8, column=4)
nC = Button(root, text="C", padx=10, pady=10, command = lambda: charClick("C"))
nC.grid(row=8, column=6)
nV = Button(root, text="V", padx=10, pady=10, command = lambda: charClick("V"))
nV.grid(row=8, column=8)
nB = Button(root, text="B", padx=10, pady=10, command = lambda: charClick("B"))
nB.grid(row=8, column=10)
nN = Button(root, text="N", padx=10, pady=10, command = lambda: charClick("N"))
nN.grid(row=8, column=12)
nM = Button(root, text="M", padx=10, pady=10, command = lambda: charClick("M"))
nM.grid(row=8, column=14)
#space between keyboards
srow8 = Label(root,text="         ")
srow8.grid(row=9,column=0,columnspan=18)

#Encryption button
eB = Button(root, text="Run Encryption", padx=2, pady=2)
eB.grid(row=12, column=14, columnspan=3)

pB = Button(root, text="Apply Plugboard", padx=2, pady=2)
pB.grid(row=15, column=14, columnspan=3)

#textboxes
clabel = Label(root,text="Encrypted Message")
clabel.grid(row=11,column=0,columnspan=18)

ctext = Entry(root,width=50,borderwidth=3)
ctext.grid(row=12,column=0,columnspan=18)

nlabel = Label(root,text="Normal Message")
nlabel.grid(row=13,column=0,columnspan=18)

ntext = Entry(root,width=50,borderwidth=3)
ntext.grid(row=14,column=0,columnspan=18)

plabel = Label(root, text="Plugboard Pairs")
plabel.grid(row=15,column=0,columnspan=18)

ptext = Entry(root,width=50, borderwidth=3)
ptext.grid(row=16,column=0,columnspan=18)

def charClick(abc):
    current = ntext.get()
    ntext.delete(0,END)
    ntext.insert(0, str(current) + str(abc))
    #print(abc)

root.mainloop()
