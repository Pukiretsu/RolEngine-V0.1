#--------------------------Library Import--------------------------#
import PySimpleGUI as gui
from os import system
import Layout 
from fractions import Fraction
#------------------------------Config------------------------------#

# TODO: Start with the server thing...
# TODO: Make a function to automatically size the launcher

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
    Variables (local)
    ----------
    Width, height (int)
        Screen actual resolution in pixels
    ratio (fraction object)
        if printed it shows a fraction where you can interpret it as "Numerator:Denominator"
        ex: 16:9 (landscape) or 4:4 (square)
    factor:
        The factor of the actual size of the app
    """
    # Get the screen actual resolution in pixels 
    width, height = gui.Window.get_screen_size()  
    ratio = Fraction(width/height).limit_denominator()
    factor = width//ratio.numerator//2
    return ratio, factor

ratio, factor = GetAspectRatio()
winSize = (ratio.numerator*factor,ratio.denominator*factor)

#------------------------Window magnagement------------------------#

window = gui.Window    (
                            title = "Chupame los cocos.",
                            layout = Layout.mainLayout,
                            auto_size_buttons = True, 
                            resizable = True,
                            no_titlebar = False,
                            grab_anywhere = True,
                            size = winSize
                        )

#------------------------Events magnagement------------------------#

fullscreen = False

while True:
    event, values = window.read()
    """ 
    system("cls")
    print(values)
    print(event)
     """
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