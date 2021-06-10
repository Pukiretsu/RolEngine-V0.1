#----------------------------TO DO list--------------------------#
'''
TODO : Start with the server thing... [Started...]
[DONE] : Make a function to automatically size the launcher and get the aspect ratio
[DONE] : automatically create a config file as a json 
TODO : Create a autentication system user and password
    TODO : First make it work locally
    TODO : Implement it with sockets (look in server.py and client.py for further info) 
TODO : Implement the base Layouts
    TODO : Implement a client layout to create their character info, Please guide yourself 
    with the template of the character sheet found on:
    https://docs.google.com/spreadsheets/d/1aM7MPZn-rG12oEk-3mI_V1b0M8uEm7EEqvN_U0CPXzs/edit?usp=sharing
    TODO : Implement a DM layout to interact with the character info
'''
#UI
'''
TODO : Start prototyping the UI
    TODO : For client
        TODO : Character Creation Assistant
            [DONE] : Basic Info
            TODO : Atribbutte info  
    TODO : For master
        TODO : Character Display 
        TODO : Character panel magnagement

TODO : Make the UI
    TODO : Algorithm to auto size and pan based on window size
    TODO : For client
        TODO : Character Creation Assistant
            TODO : Basic Info (work in progress)
            TODO : Atribbutte info  
    TODO : For master
        TODO : Character Display 
        TODO : Character panel magnagement
        
'''

#--------------------------Library Import--------------------------#
from fractions import Fraction
from os import system
from tkinter import font
from typing import Text #This is just for debugging
import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import Col, Column, Input
import Configs as conf

#-----------------------------Variable-----------------------------#
# Configuration file

if conf.DetectConfigs():
    configs = conf.GetConfigs()
else:
    conf.Defaults()
    configs = conf.GetConfigs()

# Colors and aspect

colorTheme = "Light Brown 13"
gui.theme(colorTheme)
buttonColor = ((gui.theme_element_text_color(), gui.theme_background_color()))

# Window Variables

width, height = gui.Window.get_screen_size()
scrnPercFactor = 100/((width**2 + height**2)**(1/2)) # The actual size of the vector resultant from the screen size


#-----------------------------Function------------------------------#
def GetAspectRatio():
    """ 
    Definition:
    ------------
    Gets the actual resolution of the user screen and then
    it gets their aspect ratio in the form of a fraction.
    
    Variables:
    ----------
    Width, height (int)
        Screen actual resolution in pixels
    ratio (fraction object)
        if printed it shows a fraction where you can interpret it as 
        "Numerator:Denominator" ex: 16:9 (landscape) or 4:4 (square)
    """
    ratio = Fraction(width/height).limit_denominator()
    return ratio

def GetObjectFactor():
    """ 
    Definition:
    ------------
    it makes a product of the vector normal resultant in the actual size of the screen and the window
    
    Variables:
    ----------
    newSize (Tuple)
        Window Resolution
    newWindowValue (float)

    """
    try:
        newSize = window.size
    except:
        return configs["ObjFactor"]
    newWindowValue = ((newSize[0]**2 + newSize[1]**2)**(1/2))
    return int(newWindowValue * scrnPercFactor)

def PXPTConvert(data, mode): # 4px = 3pt
    if mode == "PX":
        return round(data/4*3)
    if mode == "PT":
        return round(data/3*4)

def GetFont(parm):
    font = "BahnschriftLight"
    if parm == 'Tittle':
        return font + " " +  "50" #str(round(GetObjectFactor()*2/5))
    if parm == 'Button':
        return font + " " + "25" #str(round(GetObjectFactor()*2/5))



#------------------------------Layout------------------------------#
mainLeftColumn  =   [
    {gui.Text("Rol Engine")}
                ]

mainRightColumn =   [
    [
        gui.Text("",key='/textoPrueba/',),
        gui.Button(key="/Fullscreen/", button_text="Pantalla completa")
    ],
    [gui.Button(key="/exit/",button_text="Salir")]
                    ] 

mainLayout  =   [   
    [
        gui.Column(mainLeftColumn),
        gui.Column(mainRightColumn, justification="right")
    ]
                ]

basicInfoClient =   [
    [
        gui.Column([
                    [gui.Button()],
                    
                    [gui.Input()]
                    ]
                   #Espacio para los parametros
                   ),
        gui.Column([
                    [
                        gui.Text("Edad:"),
                        gui.Input(),
                        gui.Text("Color de piel:"),
                        gui.Input()],
                    
                    [
                        gui.Text("Estatura:"),
                        gui.Input(),
                        gui.Text("m"),
                        gui.Text("Genero:"),
                        gui.Input()
                    ],
                    
                    [gui.Text("Descripcion General")],
                    
                    [gui.Input()]
                    ]

                   )
    ],
                    ]

characterCreation   =   [
    [
        gui.Button("Basica",    key="/BASIC_INFOCLIENT/",       font = GetFont("Button"), border_width = 0, button_color = buttonColor),
        gui.Button("Atributos", key="/ATTRIBUTE_INFOCLIENT/",   font = GetFont("Button"), border_width = 0, button_color = buttonColor),
        gui.Text("Creacion de personajes", font=GetFont("Tittle"))
    ],
    
    [
        gui.Column(basicInfoClient)
    ],
    
    [
        gui.Button("Volver",    key="/BACKMAIN/",       font = GetFont("Button"), border_width = 0, button_color = buttonColor),
        gui.Button("Atributos", key="/NEXTHABILITIES/", font = GetFont("Button"), border_width = 0, button_color = buttonColor),

    ],
                        ]

#------------------------Window magnagement------------------------#

window = gui.Window    (
                            title = "Rol Engine launcher",
                            layout = characterCreation,
                            auto_size_buttons = True, 
                            resizable = True,
                            size = configs["WindowedRes"],
                            element_justification="right",
                            finalize=True,
                        )
window.bind('<Configure>',"/RESIZED/") #Binding a TKinter event to window

#------------------------Events magnagement------------------------#
window.maximize()

while True:
    event, values = window.read()
    """     system("cls") """
    print(values)
    print(event)
    
    # TODO : Detect when fullscreen
    if event == "/RESIZED/":
        print(GetObjectFactor())
        print(window.size)
        pass
    
    if event in (None, "/exit/", gui.WIN_CLOSED):
        break

window.close()