import serial
import time
import PySimpleGUI as sg
import math
import tkinter
from tkinter import *
import pymata4
from pymata4 import pymata4
from PIL import Image
from PIL import ImageTk


#arduinoData=serial.Serial('com3',115200)

def Communicate(x,y,R,phid,thetad):
    print('x= ',x)
    print('y= ',y)
    print('R= ',R)
    print('Phi= ', phid,' in degrees')
    print('Launch Angle= ',thetad,' in degrees')

    steps = round(phid/.09)
    #load command strings with thetad and steps
    cmd1 = str(thetad) + '\r'

    cmd2 = str(steps) + '\r'

    #write launch instructions to arduino
    #arduinoData.write(cmd1.encode())
    #arduinoData.write(cmd2.encode())




#variable intialization--------------------------
rc = float(1.75) #radius of the cup
g = float(-32.2)  #gravity in ft/s
ht = float(10) #idk what this is yet
v = float(84) #velocity in in/s
L = 10#float(input('Enter the length of the table in inches: '))
W = 10#float(input('Enter the width of the table in inches: '))
H = 10#float(input('Enter the height of the parabola in inches: '))
#L =  L+'\r' #this is a carage return that lets the arduino find it easy
#W = W+'\r' #this is a carage return that lets the arduino find it easy
#arduinoData.write(L.encode())
#arduinoData.write(W.encode())   

## Stepper setup ----------------------------
#num_Steps = 4096  # one step = 0.09 degrees now
#pins = [8,9,10,11]
#stepper = pymata4.Pymata4()

#stepper.set_pin_mode_stepper(num_Steps, pins)

#while True:
    #stepper.stepper_write(21, num_Steps) #21=speed
#    time.sleep(1) #delay of one second
#    stepper.stepper_write(21, -4096) #reverses the stepper
#    time.sleep(.5) #.5 sec delay

#Servo setup--------------------------------
#def servocontrol(var):
#    arduinoData.write(bytes([var])) #idk i just followed some dude who's probably indian


#create the window------------------------------
win = Tk()
win.geometry('450x450')
win.resizable(True,True)
win.title('Pong Launcher')
#cmd1 = str(0)
#cmd1 = cmd1 +'\r'
#arduinoData.write(cmd1.encode())


#creating the background---------------------------
#image = Image.open('cupformation.png')
#image = image.resize((500, 500))
#image = ImageTk.PhotoImage(image)

#canv = Canvas(win, width=80, height=80)

## Stepper Calibration step ------------------------------
# have the stepper align the launcher arm with the y axis of the table and hold for about 30 seconds to adjust it------------------------------


#arduinoData.write(stepper.encode())



#Servo Calibration step--------------------------------

#arduinoData.write(L.encode())
 

#Define and control all the buttons-------------------------------------
def btn1():
    x = (W)/2
    y = (L)-(7*rc)
    R = math.sqrt((float(x)**2)+(float(y)**2))
    phi = math.asin(float(x)/float(R))
    phid = math.degrees(phi)
    theta = (math.acos((R*g)/((v**2)*2)))/2
    thetad = math.degrees(theta)
    #stepper.stepper_write(10,phid/0.09)
    #arduinoData.write(stepper.encode())
    #arduinoData.write(W.encode()) 

    Communicate(x,y,R,phid,thetad)

    

def btn2():
    x = (W/2)-rc
    y = L-(5*rc)
    R = math.sqrt((float(x)**2)+(float(y)**2))
    phi = math.asin(float(x)/float(R))
    phid = math.degrees(phi)
    theta = (math.acos((R*g)/((v**2)*2)))/2
    thetad = math.degrees(theta)
    #stepper.stepper_write(10,phid/0.09)
    #arduinoData.write(stepper.encode())
    #arduinoData.write(servocontrol.encode()) 

    Communicate(x,y,R,phid,thetad)

def btn3():
    x = (W/2)+rc
    y = L-(5*rc)
    R = math.sqrt((float(x)**2)+(float(y)**2))
    phi = math.asin(float(x)/float(R))
    phid = math.degrees(phi)
    theta = (math.acos((R*g)/((v**2)*2)))/2
    thetad = math.degrees(theta)
    #stepper.stepper_write(10,phid/0.09)
    #arduinoData.write(stepper.encode())
    #arduinoData.write(W.encode()) 

    Communicate(x,y,R,phid,thetad)

def btn4():
    x = (W/2)+(2*rc)
    y = L-(3*rc)
    R = math.sqrt((float(x)**2)+(float(y)**2))
    phi = math.asin(float(x)/float(R))
    phid = math.degrees(phi)
    theta = (math.acos((R*g)/((v**2)*2)))/2
    thetad = math.degrees(theta)
    #stepper.stepper_write(10,phid/0.09)
    #arduinoData.write(stepper.encode())
    #arduinoData.write(W.encode())
 
    Communicate(x,y,R,phid,thetad)

def btn5():
    x = W/2
    y = L-(3*rc)
    R = math.sqrt((float(x)**2)+(float(y)**2))
    phi = math.asin(float(x)/float(R))
    phid = math.degrees(phi)
    theta = (math.acos((R*g)/((v**2)*2)))/2
    thetad = math.degrees(theta)
    #stepper.stepper_write(10,phid/0.09)
    #arduinoData.write(stepper.encode())
    #arduinoData.write(W.encode()) 

    Communicate(x,y,R,phid,thetad)

def btn6():
    x = (W/2)-(2*rc)
    y = L-(rc)
    R = math.sqrt((float(x)**2)+(float(y)**2))
    phi = math.asin(float(x)/float(R))
    phid = math.degrees(phi)
    theta = (math.acos((R*g)/((v**2)*2)))/2
    thetad = math.degrees(theta)
    #stepper.stepper_write(10,phid/0.09)
    #arduinoData.write(stepper.encode())
    #arduinoData.write(W.encode()) 

    Communicate(x,y,R,phid,thetad)

def btn7():
    x = (W/2)-(4*rc)
    y = L-(rc)
    R = math.sqrt((float(x)**2)+(float(y)**2))
    phi = math.asin(float(x)/float(R))
    phid = math.degrees(phi)
    theta = (math.acos((R*g)/((v**2)*2)))/2
    thetad = math.degrees(theta)
    #stepper.stepper_write(10,phid/0.09)
    #arduinoData.write(stepper.encode())
    #arduinoData.write(W.encode()) 

    Communicate(x,y,R,phid,thetad)

def btn8():
    x = (W/2)-rc
    y = L-(rc)
    R = math.sqrt((float(x)**2)+(float(y)**2))
    phi = math.asin(float(x)/float(R))
    phid = math.degrees(phi)
    theta = (math.acos((R*g)/((v**2)*2)))/2
    thetad = math.degrees(theta)
    #stepper.stepper_write(10,phid/0.09)
    #arduinoData.write(stepper.encode())
    #arduinoData.write(W.encode()) 

    Communicate(x,y,R,phid,thetad)

def btn9():
    x = (W/2)+rc
    y = L-(rc)
    R = math.sqrt((float(x)**2)+(float(y)**2))
    phi = math.asin(float(x)/float(R))
    phid = math.degrees(phi)
    theta = (math.acos((R*g)/((v**2)*2)))/2
    thetad = math.degrees(theta)
    #stepper.stepper_write(10,phid/0.09)
    #arduinoData.write(stepper.encode())
    #arduinoData.write(.encode()) 

    Communicate(x,y,R,phid,thetad)

def btn10():
    x = (W/2)+(4*rc)
    y = L-(rc)
    R = math.sqrt((float(x)**2)+(float(y)**2))
    phi = math.asin(float(x)/float(R))
    phid = math.degrees(phi)
    theta = (math.acos((R*g)/((v**2)*2)))/2
    thetad = math.degrees(theta)
    #stepper.stepper_write(10,phid/0.09)
    #arduinoData.write(stepper.encode())
    #arduinoData.write(.encode()) 

    Communicate(x,y,R,phid,thetad)

    #phid is converted from degrees to steps for stepper
    #phid = 180

    #theta is sent as angle in degrees for servo launch angle
    #thetad = 120


    #write reset instructions to arduino
    #cmd1 = str(0)
    #arduinoData.write(cmd1.encode())




#Creating all the buttons-----------------------------------------------------
button1 = Button(win, text="1", command=btn1).place(x=250,y=300)
button2 = Button(win, text="2", command=btn2).place(x=300,y=250)
button3 = Button(win, text="3", command=btn3).place(x=200,y=250)
button4 = Button(win, text="4", command=btn4).place(x=150,y=200)
button5 = Button(win, text="5", command=btn5).place(x=250,y=200)
button6 = Button(win, text="6", command=btn6).place(x=350,y=200)
button7 = Button(win, text="7", command=btn7).place(x=400,y=150)
button8 = Button(win, text="8", command=btn8).place(x=300,y=150)
button9 = Button(win, text="9", command=btn9).place(x=200,y=150)
button10 = Button(win, text="10", command=btn10).place(x=100,y=150)
#killButton = Button(win, text="Kill Mode",fg="red", command=killbtn).place(x=228,y=350)
win.mainloop()

