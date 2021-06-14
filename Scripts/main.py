#----------------------------TO DO list--------------------------#
'''
TODO : Start with the server thing... [Started...]
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

characterCreation = Layouts.characterCreation

#------------------------Window magnagement------------------------#

window = gui.Window    (
                            title = "Rol Engine Alpha V0.1",
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
#print("Placeholder: " ,window["PH"].get_size())
#print("Upload: " ,window["/CLIENT_AVATARUPLOAD/"].get_size())
#print("Name: " ,window["/CLIENT_CHARACTER_NAME/"].get_size())
print("Volver: "    , window["/BACKMAIN/"].get_size())
print("Siguiente: " , window["/NEXTHABILITIES/"].get_size())
print("Resolucion actual: ", window.size)

while True:
    event, values = window.read()

    #system("cls") 
    print(values) 
    print(event) 
    
    if event in (None, "/exit/", gui.WIN_CLOSED,"/BACKMAIN/"):
        break
window.close()
