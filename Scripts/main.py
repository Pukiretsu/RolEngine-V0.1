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

#--------------------------Library Import--------------------------#
from fractions import Fraction
from os import system #This is just for debugging 
import PySimpleGUI as gui
import Configs as conf
import Layouts
#-----------------------------Variable-----------------------------#
# Configuration file

if conf.DetectConfigs():
    configs = conf.GetConfigs()
else:
    conf.Defaults()
    configs = conf.GetConfigs()

# Window Variables

width, height = gui.Window.get_screen_size()

""" def GetFont(parm):
    if parm == 'Tittle':
        return font + " " + "50" #str(round(GetObjectFactor()*2/5))
    if parm == 'Button':
        return font + " " + "25" #str(round(GetObjectFactor()*2/5))
 """
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

characterCreation = Layouts.characterCreation

#------------------------Window magnagement------------------------#

window = gui.Window    (
                            title = "Rol Engine launcher",
                            layout = characterCreation,
                            auto_size_buttons = True,
                            size = configs["WindowedRes"],
                            element_justification = "left",
                            finalize = True,
                            margins = (0,10)
                        )
#window.bind('<Configure>',"/RESIZED/") #Binding a TKinter event to window

#------------------------Events magnagement------------------------#
""" n = 50
num = []
for number in range(1,n+1):
    num.append(number)
event, values = window.read(timeout=100)
for size in num:
    ActualFont = Layouts.fonts["Font"] + str(size)
    window["/CLIENT_CHARCRTITTLE/"].update(font=ActualFont) 
    window.refresh()
    print(ActualFont, ": " ,window["/CLIENT_CHARCRTITTLE/"].get_size(), "\n")
    event, values = window.read(timeout=100) """

window.refresh()
print("Basica: ",window["/CLIENT_BASICINFO/"].get_size())
print("Atributos: ",window["/CLIENT_ATTRIBUTEINFO/"].get_size())
print("Titulo: ",window["/CLIENT_CHARCRTITTLE/"].get_size())
print("Resolucion actual: ", window.size)
while True:
    event, values = window.read()

    system("cls") 
    print(values) 
    print(event) 
    
    # TODO : Detect when fullscreen
    if event == "/RESIZED/":
        pass
    if event == "/CLIENT_BASICINFO/":
        pass
    if event == "/CLIENT_ATTRIBUTEINFO/":
        window.refresh()
        print("Titulo: ",window["/CLIENT_CHARCRTITTLE/"].get_size())
        pass
    
    if event in (None, "/exit/", gui.WIN_CLOSED):
        break
window.close()
