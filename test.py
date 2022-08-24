import serial
import PySimpleGUI as sg
import math
import tkinter
from tkinter import *
#from PIL import ImageTK, Image


#arduinoData=serial.Serial('com3',9600)

#variable intialization
rc = float(1.75) #radius of the cup
g = float(32.2)  #gravity in ft/s
ht = float(10) #idk what this is yet
L = float(input('Enter the length of the table in inches: '))
W = float(input('Enter the width of the table in inches: '))
H = float(input('Enter the height of the parabola in inches: '))
#L =  L+'\r' #this is a carage return that lets the arduino find it easy
#W = W+'\r' #this is a carage return that lets the arduino find it easy
#arduinoData.write(L.encode())
#arduinoData.write(W.encode())   

#create the window
win = Tk()
win.geometry('350x350')
win.resizable(True,True)
win.title('Pong Launcher')

#place image
#img = ImageTk.PhotoImage(Image.open("cupformation.jpg"))

while True:

    def btn1():
        x = (W)/2
        y = (L)-(7*rc)
        print('x= ',x)
        print('y= ',y)

    def btn2():
        x = (W/2)-rc
        y = L-(5*rc)
        print('x= ',x)
        print('y= ',y)

    def btn3():
        x = (W/2)+rc
        y = L-(5*rc)
        print('x= ',x)
        print('y= ',y)

    def btn4():
        x = (W/2)+(2*rc)
        y = L-(3*rc)
        print('x= ',x)
        print('y= ',y)

    def btn5():
        x = W/2
        y = L-(3*rc)
        print('x= ',x)
        print('y= ',y)

    def btn6():
        x = (W/2)-(2*rc)
        y = L-(rc)
        print('x= ',x)
        print('y= ',y)

    def btn7():
        x = (W/2)-(4*rc)
        y = L-(rc)
        print('x= ',x)
        print('y= ',y)

    def btn8():
        x = (W/2)-rc
        y = L-(rc)
        print('x= ',x)
        print('y= ',y)

    def btn9():
        x = (W/2)+rc
        y = L-(rc)
        print('x= ',x)
        print('y= ',y)

    def btn10():
        x = (W/2)+(4*rc)
        y = L-(rc)
        print('x= ',x)
        print('y= ',y)

#Creating all the buttons
    button1 = Button(win, text="1", command=btn1)
    button1.pack()
    button2 = Button(win, text="2", command=btn2)
    button2.pack()
    button3 = Button(win, text="3", command=btn3)
    button3.pack()
    button4 = Button(win, text="4", command=btn4)
    button4.pack()
    button5 = Button(win, text="5", command=btn5)
    button5.pack()
    button6 = Button(win, text="6", command=btn6)
    button6.pack()
    button7 = Button(win, text="7", command=btn7)
    button7.pack()
    button8 = Button(win, text="8", command=btn8)
    button8.pack()
    button9 = Button(win, text="9", command=btn9)
    button9.pack()
    button10 = Button(win, text="10", command=btn10)
    button10.pack()
    win.mainloop()

    R = math.sqrt((float(x)**2)+(float(y)**2))
    #phi = math.asin(int(x)/int(R))
    print('R= ', R)
    #print(phi)

win = Tk()