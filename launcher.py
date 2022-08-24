import serial
import PySimpleGUI as sg
import math
import tkinter as tk


#arduinoData=serial.Serial('com3',9600)

#variable intialization
rc = int(1.75) #radius of the cup
g = int(32.2)  #gravity in ft/s
ht = int(10) #idk what this is yet
global x
global y
x = 0
y = 0
L = input('Enter the length of the table in inches: ')
W = input('Enter the width of the table in inches: ')
H = input('Enter the height of the parabola in inches: ')
#L =  L+'\r' #this is a carage return that lets the arduino find it easy
#W = W+'\r' #this is a carage return that lets the arduino find it easy
#arduinoData.write(L.encode())
#arduinoData.write(W.encode())   
L = int(L)
W = int(W)
H = int(H)

    #### Once the length and width are told, the U/I should pop up for cup selection, when the cup is selected, the math will be done.
    #USER INTERFACE and LOOP for Window
def make_window(theme=None):
    layout = [
            [sg.Text("Please select a cup"),
            sg.Button(button_text='1', button_color=('white','black')),
            sg.Button(button_text='2', button_color=('white','black')),
            sg.Button(button_text='3', button_color=('white','black')),
            sg.Button(button_text='4', button_color=('white','black')),
            sg.Button(button_text='5', button_color=('white','black')),
            sg.Button(button_text='6', button_color=('white','black')),
            sg.Button(button_text='7', button_color=('white','black')),
            sg.Button(button_text='8', button_color=('white','black')),
            sg.Button(button_text='9', button_color=('white','black')),
            sg.Button(button_text='10', button_color=('white','black'))]
            ]

    window = sg.Window("Pong Launcher", layout, margins=(350,350))
    return window

window = make_window()

while True:
    cup_choice = window.read()
    if cup_choice == sg.WIN_CLOSED :
        break
    elif cup_choice == '1':
                x = (W)/2
                y = (L)-(7*rc)
                window.close()
                print('x= ',x)
                print('y= ',y)
                sg.WIN_CLOSED 
                         
    elif cup_choice == '2':
                x = W/2
                y = L-(7*rc)
                window.close()
                
    elif cup_choice == '3':
                x = W/2
                y = L-(7*rc)
                window.close()
                
    elif cup_choice == '4':
                x = W/2
                y = L-(7*rc)
                window.close()
                
    elif cup_choice == '5':
                x = W/2
                y = L-(7*rc)
                window.close()
                
    elif cup_choice == '6':
                x = W/2
                y = L-(7*rc)
                window.close()
               
    elif cup_choice == '7':
                x = W/2
                y = L-(7*rc)
                window.close()
               
    elif cup_choice == '8':
                x = W/2
                y = L-(7*rc)
                window.close()
                
    elif cup_choice == '9':
                x = W/2
                y = L-(7*rc)
                window.close()
                
    elif cup_choice == '10':
                x = W/2
                y = L-(7*rc)
                window.close()
                
    
    

    R = math.sqrt((int(x)**2)+(int(y)**2))
    #phi = math.asin(int(x)/int(R))
    print('R= ', R)
    #print(phi)
 