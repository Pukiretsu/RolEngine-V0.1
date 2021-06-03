#----------------------------TO DO list--------------------------#
'''
TODO : Start with the server thing... [Started...]
[DONE] : Make a function to automatically size the launcher and get the aspect ratio
[DONE] : automatically create a config file as a json 
TODO : Create a autentication system user and password
    TODO : First make it work locally
    TODO : Implement it with sockets (look in server.py and client.py for further info) 
'''

#--------------------------Library Import--------------------------#
from tkinter.constants import TRUE
import PySimpleGUI as gui
from os import system
import Layout 
from fractions import Fraction
import Configs as conf

#------------------------------Config------------------------------#

if conf.DetectConfigs():
    configs = conf.GetConfigs()
else:
    conf.Defaults()
    configs = conf.GetConfigs()

#--------------------------Window Size set-------------------------#

def GetAspectRatio():
    """ 
    Definition:
    ------------
    Gets the actual resolution of the user screen and then
    it gets their aspect ratio in the form of a fraction and then
    gets the factor of the actual size of the app in windowed mode
    this factor is actualy the screen size at half resolution just adjusted at
    every possible monitor.
    
    Variables:
    ----------
    Width, height (int)
        Screen actual resolution in pixels
    ratio (fraction object)
        if printed it shows a fraction where you can interpret it as 
        "Numerator:Denominator" ex: 16:9 (landscape) or 4:4 (square)
    factor:
        The factor of the actual windowed size of the app
    """
    width, height = gui.Window.get_screen_size()  
    ratio = Fraction(width/height).limit_denominator()
    factor = width//ratio.numerator//2
    return ratio, factor

ratio, factor = GetAspectRatio()
winSize = (ratio.numerator*factor,ratio.denominator*factor)
GetAspectRatio()

#------------------------Window magnagement------------------------#

window = gui.Window    (
                            title = "Rol Engine launcher",
                            layout = Layout.mainLayout,
                            auto_size_buttons = True, 
                            resizable = True,
                            no_titlebar = False,
                            grab_anywhere = True,
                            size = winSize
                        )

#------------------------Events magnagement------------------------#



while True:
    event, values = window.read()

    system("cls")
    print(values)
    print(event)
    
    if event in (None, "/exit/", gui.WIN_CLOSED):
        break

window.close()