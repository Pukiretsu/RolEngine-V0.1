#--------------------------Library Import--------------------------#
from tkinter.constants import FALSE
import PySimpleGUI as gui
from os import system
import Layouts
#------------------------------Config------------------------------#

# TODO: Start with the server thing...

#------------------------Window magnagement------------------------#

window = gui.Window    (
                            title = "Chupame los cocos.",
                            layout = Layouts.mainLayout,
                            auto_size_buttons = True, 
                            resizable = True,
                            no_titlebar=False,
                            grab_anywhere=True
                        )

#------------------------Events magnagement------------------------#

fullscreen = False

while True:
    event, values = window.read()
    
    system("cls")
    print(values)
    print(event)
    
    if event == "/Fullscreen/":
        if fullscreen == False:
            window.maximize()
            window["/Fullscreen/"].update(text="Ventana")
            fullscreen = True
            
        else:
            window.normal()
            window["/Fullscreen/"].update(text="Pantalla completa")
            fullscreen = False
            
    
    if event in (None, "/exit/", gui.WIN_CLOSED):
        break

window.close()