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
from PySimpleGUI.PySimpleGUI import T
import Configs as conf
import GFXMagnagement as gfx
import Layouts
#-----------------------------Variable-----------------------------#
# Configuration file
if conf.DetectConfigs():
    configs = conf.GetConfigs()
else:
    conf.Defaults()
    configs = conf.GetConfigs()
    
characterCreation = Layouts.characterCreation

ccInputsKeys = ["/CLIENT_CHARACTER_NAME/", "/CLIENT_CHARACTER_AGE/", "/CLIENT_CHARACTER_HEIGHT/", "/CLIENT_CHARACTER_RACE/", "/CLIENT_CHARACTER_GENDER/"]
ccDefValues = ["Nombre", "Años", "Metros", "Seleccione",]

class Player:
    def __init__(self,basicInfo: tuple) -> None:
        self.name:      basicInfo[0]
        self.age:       basicInfo[1]
        self.height:    basicInfo[2]
        self.race:      basicInfo[3]
        self.gender:    basicInfo[4]
    
    def parse_info(self):
        # TODO : Write the method xd
        pass


#------------------------Window magnagement------------------------#
window = gui.Window    (
                            title = "Rol Engine Alpha V0.1",
                            layout = characterCreation,
                            auto_size_buttons = True,
                            size = configs["WindowedRes"],
                            element_justification = "left",
                            finalize = True,
                            margins = (0,5)
                        )
#------------------------Events magnagement------------------------#

window.refresh()
print("Resolucion: ",window.size)
print(window["/CLIENT_CHARACTER_DESCRIPTION/"].get_size())
print(Layouts.scales['R_CHCDesc'])

LayoutPos = "CHC_PLAYERINFO"

def debug(evn, val):
    print(val) 
    print(evn) 
    

while True:
    event, values = window.read()
    debug(event,values)

    if event == "/CLIENT_ATTRIBUTEINFO/":
        window["/CLIENT_BASICINFO/"].update(button_color = Layouts.colors['InactiveTab'])
        window["/CLIENT_ATTRIBUTEINFO/"].update(button_color = Layouts.colors['ActiveTab'])
        
        window["/PLAYERINFO_LAYOUT/"].update(visible=False)
        window["/PLAYERATTINFO_LAYOUT/"].update(visible=True)
        window.finalize()
        
            
    if event == "/CLIENT_BASICINFO/":
        window["/CLIENT_ATTRIBUTEINFO/"].update(button_color = Layouts.colors['InactiveTab'])
        window["/CLIENT_BASICINFO/"].update(button_color = Layouts.colors['ActiveTab'])

        window["/PLAYERATTINFO_LAYOUT/"].update(visible=False)
        window["/PLAYERINFO_LAYOUT/"].update(visible=True)
        window.finalize()

    if event == "/CLIENT_AVATARUPLOAD/":
        imgPath = values['/CLIENT_AVATARUPLOAD/']
        avatarCrop = gfx.PNGCircleCrop(imgPath,None,Layouts.scales['S_CHCAvatar'])
        avatarBytes = gfx.PNG_EncodedBase64(avatarCrop)
        window["/CLIENT_AVATAR/"].update(data=avatarBytes)
        window.finalize()
    
    if event in ccInputsKeys:
        """
        This verifies if the player has filled correctly all input spaces
        """
        for key in ccInputsKeys:
            if values[key] not in ccDefValues and values[key] != "":
                window["/NEXTHABILITIES/"].update(disabled=False)
            elif values[key] in ccDefValues or values[key] == "":
                window["/NEXTHABILITIES/"].update(disabled=True)
                break
            

    if event in (None, "/exit/", gui.WIN_CLOSED,"/BACKMAIN/"):
        break
window.close()
