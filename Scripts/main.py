#--------------------------Library Import--------------------------#
from tkinter.constants import FALSE
import PySimpleGUI as gui
<<<<<<< HEAD
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
=======
from os import system
import Layouts
#------------------------------Config------------------------------#
>>>>>>> 2f4f049519b1be6aac6945a06b325452f0d1dd4f

# TODO: Start with the server thing...

#------------------------Window magnagement------------------------#

window = gui.Window    (
<<<<<<< HEAD
                            title = "Rol Engine Alpha V0.1",
                            layout = characterCreation,
                            auto_size_buttons = True,
                            size = configs["WindowedRes"],
                            element_justification = "left",
                            finalize = True,
                            margins = (0,5)
=======
                            title = "Chupame los cocos.",
                            layout = Layouts.mainLayout,
                            auto_size_buttons = True, 
                            resizable = True,
                            no_titlebar=False,
                            grab_anywhere=True
>>>>>>> 2f4f049519b1be6aac6945a06b325452f0d1dd4f
                        )

#------------------------Events magnagement------------------------#

fullscreen = False

while True:
    event, values = window.read()
    
<<<<<<< HEAD
    
    
    if event == "/CLIENT_AVATARUPLOAD/":
        imgPath = values['/CLIENT_AVATARUPLOAD/']
        newAvatar = gfx.CircleCrop(imgPath,Layouts.scales['S_CHCAvatar'])
        newAvatar = gfx.PNG_EncodedBase64(newAvatar)
        window["/CLIENT_AVATAR/"].update(data=newAvatar)
        window.refresh()
    
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
=======
    system("cls")
    print(values)
    print(event)
    
    if event == "/Fullscreen/":
        if fullscreen == False:
            window.maximize()
            window["/Fullscreen/"].update(text="Ventana")
            fullscreen = True
>>>>>>> 2f4f049519b1be6aac6945a06b325452f0d1dd4f
            
        else:
            window.normal()
            window["/Fullscreen/"].update(text="Pantalla completa")
            fullscreen = False
            
    
    if event in (None, "/exit/", gui.WIN_CLOSED):
        break

window.close()