

from tkinter import*
from tkinter import Label

import pygame
from PIL import ImageTk ,Image

from tkinter import *
from PIL import ImageTk ,Image



pygame.init()
root=Tk()
root.title("who wants to be a Millionaire")
root.geometry('1352x652+0+0')
root.configure(background='black')

ABC = Frame(root, bg= 'black')
ABC.grid()

ABC1 =Frame (root, bg='black', bd=20, width=900, height=600)
ABC1.grid(row=0,column=0)
ABC2= Frame(root, bg='blue',bd=20,width=452,height=600)
ABC2.grid(row=0,column=1)

ABC1a =Frame (ABC1, bg='green', bd=20, width=900, height=200)
ABC1a.grid(row=0,column=0)
ABC1b =Frame (ABC1, bg='black', bd=20, width=900, height=200)
ABC1b.grid(row=1,column=0)
ABC1c =Frame (ABC1, bg='black', bd=20, width=900, height=200)
ABC1c.grid(row=2,column=0)


def Millionpicture15():
    img.destroy()
    imagephone1 = Image.open("money15.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)




def Question15():
    Queastion15= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion15.set("Which of the following is not the energy stored in a capacitor?")
    Answer1.set("CV22")
    Answer2.set(" QV2")
    Answer3.set("Q22C ")
    Answer4.set("QC2")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion15)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1,command=Millionpicture15)
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3)
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4 )
    textQuestion3.grid(row=2, column=3, pady=4)




###################################################


def Millionpicture14():
    img.destroy()
    imagephone1 = Image.open("money14.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)
    Question15()



def Question14():
    Queastion14= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion14.set("Energy stored in an inductor is ____")
    Answer1.set("LI")
    Answer2.set(" LI2")
    Answer3.set("LI/2")
    Answer4.set("LI2/2")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion14)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1,command=Millionpicture14 )
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3)
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4 )
    textQuestion3.grid(row=2, column=3, pady=4)


####################################

def Millionpicture13():
    img.destroy()
    imagephone1 = Image.open("money13.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)
    Question14()



def Question13():
    Queastion13= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion13.set("Inductance of an inductor is inversely proportional to its _____")
    Answer1.set("Number of turns")
    Answer2.set("Area of cross section")
    Answer3.set("Absolute permeability ")
    Answer4.set("Length")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion13)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1)
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3,command=Millionpicture13)
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4 )
    textQuestion3.grid(row=2, column=3, pady=4)

##############################

def Millionpicture12():
    img.destroy()
    imagephone1 = Image.open("money12.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)
    Question13()



def Question12():
    Queastion12= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion12.set("Unit of inductance is ____")
    Answer1.set("Weber ")
    Answer2.set(" Henry")
    Answer3.set("Farad ")
    Answer4.set("Tesla")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion12)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1)
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2, comnand=Millionpicture12)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3)
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4 )
    textQuestion3.grid(row=2, column=3, pady=4)

##########################################################

def Millionpicture11():
    img.destroy()
    imagephone1 = Image.open("money11.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)
    Question12()


def Question11():
    Queastion11= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion11.set("If there are N nodes in a circuit, then the number of nodal equations that can be formed are?")
    Answer1.set(" N+1 ")
    Answer2.set("N")
    Answer3.set(" N-1")
    Answer4.set(" N-2")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion11)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1)
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3 ,command=Millionpicture11)
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4 )
    textQuestion3.grid(row=2, column=3, pady=4)


##############
def Millionpicture10():
    img.destroy()
    imagephone1 = Image.open("money10.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)
    Question11()



def Question10():
    Queastion10= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion10.set("To simply matters, we shall assume in nodal analysis that circuit don't contain")
    Answer1.set(" current circuits")
    Answer2.set("resistor  circuit")
    Answer3.set(" transistor circuit")
    Answer4.set("voltage Circuit")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion10)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1)
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3)
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4 ,command=Millionpicture10)
    textQuestion3.grid(row=2, column=3, pady=4)





###########
def Millionpicture9():
    img.destroy()
    imagephone1 = Image.open("money9.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)
    Question10()

def Question9():
    Queastion9= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion9.set("Determine which of the following statement is true about mesh and loops.")
    Answer1.set("Mesh can be loop and loops also can be mesh.")
    Answer2.set("Mesh can be loop but loop cannot be mesh.")
    Answer3.set(" Mesh cannot be loop but loop can be mesh.")
    Answer4.set("none of these")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion9)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1)
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3,command=Millionpicture9)
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4 )
    textQuestion3.grid(row=2, column=3, pady=4)



#######################################

def Millionpicture8():
    img.destroy()
    imagephone1 = Image.open("money8.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)
    Question9()

def Question8():
    Queastion8= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion8.set("Supermesh is a circuit sorting that avoids source current because?")
    Answer1.set("the terminal voltage is unknown")
    Answer2.set("the terminal current is unknown")
    Answer3.set(" the terminal resistance is unknown")
    Answer4.set("the terminal impedance is unknown")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion8)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1,command=Millionpicture8 )
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3)
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4 )
    textQuestion3.grid(row=2, column=3, pady=4)


def Millionpicture7():
    img.destroy()
    imagephone1 = Image.open("money7.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)
    Question8()

def Question7():
    Queastion7= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion7.set("If there is a current source in loop, then the mesh is turned into")
    Answer1.set("Superposition")
    Answer2.set("Supernode-mesh")
    Answer3.set("supermesh")
    Answer4.set("supernode")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion7)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1, )
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3,command=Millionpicture8 )
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4 )
    textQuestion3.grid(row=2, column=3, pady=4)


##############

def Millionpicture6():
    img.destroy()
    imagephone1 = Image.open("money6.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)
    Question7()

def Question6():
    Queastion6= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion6.set("Nodal analysis can be applied for non planar network also?")
    Answer1.set("False")
    Answer2.set("True")
    Answer3.set("Both")
    Answer4.set("none of this")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion6)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1, )
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2,command=Millionpicture6)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3)
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4 )
    textQuestion3.grid(row=2, column=3, pady=4)




###########
def Millionpicture5():
    img.destroy()
    imagephone1 = Image.open("money5.png")
    photo = ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image=photo)
    img1.image = photo
    img1.place(x=960, y=50)
    Question6()

def Question5():
    Queastion5= StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion5.set("If there are 5 nodes in the circuit ,we can get______  number of euation  in the nodal analysis ")
    Answer1.set("5")
    Answer2.set("3")
    Answer3.set("6")
    Answer4.set("4")
    textQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                         textvariable=Queastion5)
    textQuestion.grid(row=0, column=0, columnspan=4, pady=4)

    lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5, justify=CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

    textQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer1, )
    textQuestion1.grid(row=1, column=1, pady=4)

    lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionB.grid(row=1, column=2, pady=4, sticky=W)
    textQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer2)
    textQuestion2.grid(row=1, column=3, pady=4)

    lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer3)
    textQuestion3.grid(row=2, column=1, pady=4)

    lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5, justify=LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                           justify=CENTER, textvariable=Answer4,command=Millionpicture5)
    textQuestion3.grid(row=2, column=3, pady=4)


##############

def Millionpicture4():
    img.destroy()
    imagephone1 = Image.open("money4.png")
    photo= ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image = photo)
    img1.image = photo
    img1.place(x=960,y=50)
    Question5()



def Question4():

    Queastion4 = StringVar()


    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion4.set("What Law Does Nodal Analysis uses?")
    Answer1.set("Kirchoffs Current Law")
    Answer2.set("Kirchoffs Voltage Law")
    Answer3.set("Both of these")
    Answer4.set("None of These")
    textQuestion = Entry(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=5,width=44,justify =CENTER ,textvariable=Queastion4)
    textQuestion.grid(row=0,column=0,columnspan=4, pady=4 )

    lblQuestionA = Label(ABC1c,font=('arial',14,'bold'),text="A: ",bg='black', fg='white',bd=5,justify =CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4,sticky=W)

    textQuestion1 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER,textvariable= Answer1 ,command=Millionpicture4   )
    textQuestion1.grid(row=1,column=1, pady=4 )

    lblQuestionB = Label(ABC1c,font=('arial',14,'bold'),text="B: ",bg='black', fg='white',bd=5,justify =LEFT)
    lblQuestionB.grid(row=1, column=2,pady=4 , sticky=W)
    textQuestion2 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER, textvariable= Answer2 )
    textQuestion2.grid(row=1,column=3, pady=4 )

    lblQuestionC = Label(ABC1c,font=('arial',14,'bold'),text="C: ",bg='black', fg='white',bd=5,justify =LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER ,textvariable= Answer3 )
    textQuestion3.grid(row=2,column=1, pady=4 )

    lblQuestionD = Label(ABC1c,font=('arial',14,'bold'),text="D: ",bg='black', fg='white',bd=5,justify =LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER,textvariable= Answer4 )
    textQuestion3.grid(row=2,column=3, pady=4 )


def Millionpicture3():
    img.destroy()
    imagephone1 = Image.open("money3.png")
    photo= ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image = photo)
    img1.image = photo
    img1.place(x=960,y=50)
    Question4()

def Question3():

    Queastion3 = StringVar()


    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion3.set("Energy per unit charge is ______ ")
    Answer1.set("current")
    Answer2.set("Voltage")
    Answer3.set("Power")
    Answer4.set("cAPICITANCE")
    textQuestion = Entry(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=5,width=44,justify =CENTER ,textvariable=Queastion3)
    textQuestion.grid(row=0,column=0,columnspan=4, pady=4 )

    lblQuestionA = Label(ABC1c,font=('arial',14,'bold'),text="A: ",bg='black', fg='white',bd=5,justify =CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4,sticky=W)

    textQuestion1 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER,textvariable= Answer1   )
    textQuestion1.grid(row=1,column=1, pady=4 )

    lblQuestionB = Label(ABC1c,font=('arial',14,'bold'),text="B: ",bg='black', fg='white',bd=5,justify =LEFT)
    lblQuestionB.grid(row=1, column=2,pady=4 , sticky=W)
    textQuestion2 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER, textvariable= Answer2 )
    textQuestion2.grid(row=1,column=3, pady=4 )

    lblQuestionC = Label(ABC1c,font=('arial',14,'bold'),text="C: ",bg='black', fg='white',bd=5,justify =LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER ,textvariable= Answer3,command=Millionpicture3)
    textQuestion3.grid(row=2,column=1, pady=4 )

    lblQuestionD = Label(ABC1c,font=('arial',14,'bold'),text="D: ",bg='black', fg='white',bd=5,justify =LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER,textvariable= Answer4 )
    textQuestion3.grid(row=2,column=3, pady=4 )





def Millionpicture2():
    img.destroy()
    imagephone1 = Image.open("money2.png")
    photo= ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image = photo)
    img1.image = photo
    img1.place(x=960,y=50)
    Question3()
def Question2():
    Queastion1 = StringVar()
    Queastion2 = StringVar()
    Queastion3 = StringVar()
    Queastion4 = StringVar()

    Answer1 = StringVar()
    Answer2 = StringVar()
    Answer3 = StringVar()
    Answer4 = StringVar()

    Queastion2.set("The of  amount voltage in closed circuit is ")
    Answer1.set("o")
    Answer2.set("1")
    Answer3.set("2")
    Answer4.set("7")
    textQuestion = Entry(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=5,width=44,justify =CENTER ,textvariable=Queastion2)
    textQuestion.grid(row=0,column=0,columnspan=4, pady=4 )

    lblQuestionA = Label(ABC1c,font=('arial',14,'bold'),text="A: ",bg='black', fg='white',bd=5,justify =CENTER)
    lblQuestionA.grid(row=1, column=0, pady=4,sticky=W)

    textQuestion1 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER,textvariable= Answer1 ,command=Millionpicture2  )
    textQuestion1.grid(row=1,column=1, pady=4 )

    lblQuestionB = Label(ABC1c,font=('arial',14,'bold'),text="B: ",bg='black', fg='white',bd=5,justify =LEFT)
    lblQuestionB.grid(row=1, column=2,pady=4 , sticky=W)
    textQuestion2 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER, textvariable= Answer2 )
    textQuestion2.grid(row=1,column=3, pady=4 )

    lblQuestionC = Label(ABC1c,font=('arial',14,'bold'),text="C: ",bg='black', fg='white',bd=5,justify =LEFT)
    lblQuestionC.grid(row=2, column=0, sticky=W)
    textQuestion3 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER ,textvariable= Answer3 )
    textQuestion3.grid(row=2,column=1, pady=4 )

    lblQuestionD = Label(ABC1c,font=('arial',14,'bold'),text="D: ",bg='black', fg='white',bd=5,justify =LEFT)
    lblQuestionD.grid(row=2, column=2, sticky=W)
    textQuestion3 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER,textvariable= Answer4 )
    textQuestion3.grid(row=2,column=3, pady=4 )





def Millionpicture1():
    img.destroy()
    imagephone1 = Image.open("money1.jpg")
    photo= ImageTk.PhotoImage(imagephone1)
    img1: Label = Label(image = photo)
    img1.image = photo
    img1.place(x=960,y=50)
    Question2()


image= Image.open("logo1.jpg")
photo= ImageTk.PhotoImage(image)
img: Label = Label(image = photo)
img.image = photo
img.Centre =Button(ABC1b, image =ImageTk.PhotoImage(image), bg='black',width=300,height=200)
img.place(x=330,y=250)
img.Centre.grid()

image50_50 = Image.open("50'50.jpg")
photo= ImageTk.PhotoImage(image50_50)
img: Label = Label(image = photo,)
img.image = photo
img.place(x=200,y=100)



imagephone = Image.open("phone.jpg")
photo= ImageTk.PhotoImage(imagephone)
img: Label = Label(image = photo)
img.image = photo

img.place(x=600,y=100)

imagepeople = Image.open("people.jpg")
photo= ImageTk.PhotoImage(imagepeople)
img: Label = Label(image = photo)
img.image = photo

img.place(x=400,y=100)


imagemoney = Image.open("money.png")
photo= ImageTk.PhotoImage(imagemoney)
img: Label = Label(image = photo)
img.image = photo
img.place(x=960,y=50)


Queastion1 = StringVar()
Queastion2 = StringVar()
Queastion3 = StringVar()
Queastion4 = StringVar()

Answer1 =StringVar()
Answer2 =StringVar()
Answer3 =StringVar()
Answer4 =StringVar()

Queastion1.set("Q1: what is ohms law ?")
Answer1.set("R")
Answer2.set("v=ir")
Answer3.set("H")
Answer4.set("i")





# Queastion2.set("The of  amount voltage in closed circuit is ")
# Answer1.set("o")
# Answer2.set("1")
# Answer3.set("2")
# Answer4.set("7")











textQuestion = Entry(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=5,width=44,justify =CENTER ,textvariable=Queastion1)
textQuestion.grid(row=0,column=0,columnspan=4, pady=4 )

lblQuestionA = Label(ABC1c,font=('arial',14,'bold'),text="A: ",bg='black', fg='white',bd=5,justify =CENTER)
lblQuestionA.grid(row=1, column=0, pady=4,sticky=W)

textQuestion1 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER,textvariable= Answer1  )
textQuestion1.grid(row=1,column=1, pady=4 )

lblQuestionB = Label(ABC1c,font=('arial',14,'bold'),text="B: ",bg='black', fg='white',bd=5,justify =LEFT)
lblQuestionB.grid(row=1, column=2,pady=4 , sticky=W)
textQuestion2 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER, textvariable= Answer2 ,command=Millionpicture1)
textQuestion2.grid(row=1,column=3, pady=4 )

lblQuestionC = Label(ABC1c,font=('arial',14,'bold'),text="C: ",bg='black', fg='white',bd=5,justify =LEFT)
lblQuestionC.grid(row=2, column=0, sticky=W)
textQuestion3 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER ,textvariable= Answer3 )
textQuestion3.grid(row=2,column=1, pady=4 )

lblQuestionD = Label(ABC1c,font=('arial',14,'bold'),text="D: ",bg='black', fg='white',bd=5,justify =LEFT)
lblQuestionD.grid(row=2, column=2, sticky=W)
textQuestion3 = Button(ABC1c ,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2 ,justify =CENTER,textvariable= Answer4 )
textQuestion3.grid(row=2,column=3, pady=4 )
#############################gg






root.mainloop()


