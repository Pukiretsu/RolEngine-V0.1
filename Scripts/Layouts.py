'''
USE
------
This script is where al the graphical layouts should be
'''
#----------------------------TO DO list--------------------------#
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
    [DONE] : Algorithm to auto size and pan based on window size
    [DONE] : Use pillow to make a user upload their own image
    TODO : For client
        TODO : Character Creation Assistant
            [DONE] : Basic Info (work in progress)
            TODO : Atribbutte info
                TODO : Pad every element  
                TODO : Rewrite every Att icon
                
    TODO : For master
        TODO : Character Display 
        TODO : Character panel magnagement
        
'''

#--------------------------Library Import--------------------------#

import PySimpleGUI as gui
import Configs as conf
from math import ceil
import GFXMagnagement as gfx

#---------------------------Variable Def---------------------------#

if conf.DetectConfigs():
    configs = conf.GetConfigs()
else:
    conf.Defaults()
    configs = conf.GetConfigs()

# Color and font Dicts

colors = {
    'Theme' : "Light Brown 13", # Internal Theme of Pysimplegui
    }

fonts = {
    'Font' : "BahnschriftLight ", #The family of the font
    # Text fonts
    'TFnt' : 7.4, # Tittles 
    'STFnt' : 5, # SubTittle 
    'IFnt' : 5, # Input enter
    'FormFnt' : 6, # Age input 
    # Element fonts
    'BFnt' : 3.5, # Buttons 
    'CtrlFnt' : 4.2, # Proced and Back button 
    'TabFnt' : 4.4, # Button type Tab 
    }

scales = {
    'S_CHCAvatar' : 35, # Picture
    'S_CHCAtributeRsc' : 20, # Picture
    'R_CHCDesc': (45,fonts['FormFnt']), #  Rows
}

# This last one is very special, the spacings have codes and the values are listed in the pdf

spacing = {
    'W_CHCMarGins' : 1.5, # Margins of the row
    'W_CHCCenterTittle' : 40, # The central between The buttons and the tittle
    'W_CHCAvatar': 3.5,
    'W_CHCNAME' : 9, # Name input field 
    'W_CHCAvatarUpload': 16.04,
    'W_Controls': 81 ,
    'W_CHCInputSEP': 1,
    'H_CHCMotd' : 1, # Over the subtitle
    'H_CHCAvatar': 2.5,
    'H_CHCInputSEP': 4.9,
}

#-----------------------------Function------------------------------#
def setFactors(dct):
    '''
    Definition:
    ------------
    Takes all the percentages put in the dict and rewrittes every value
    converting them to pixel space related to the actual window size
    
    '''
    widthFactor = configs["WindowedRes"][0]/100
    heightFactor = configs["WindowedRes"][1]/100
    for Space in dct:
        if Space[0] == "W": # Widh space
            dct[Space] *= widthFactor
        
        elif Space[0] == "H": # Height space
            dct[Space] *= heightFactor
        
        elif Space[0] == "S": # Square Scale
            value = dct[Space] * widthFactor
            dct[Space] = (int(value),int(value))
        
        elif Space[0] == "R": # Rows Factor
            boxSize = dct[Space][0] * heightFactor
            fntSize = dct[Space][1] * heightFactor
            
            dct[Space] = int(ceil(boxSize/fntSize))

def setFontSizing(FNTs):
    HeightFactor = configs["WindowedRes"][1]/100
    for size in FNTs:
        if size != 'Font':
            value = 0.6697 * (FNTs[size]*HeightFactor) - 3.1135 # That comes from a linear regression of the Pt vs Px values
            FNTs[size] = FNTs["Font"] + str(round(value))

def setResources(rsc):
    for resource in rsc:
        if resource[0] == "C":
            cropedImg = gfx.PNGCircleCrop(None, rsc[resource], scales['S_CHCAvatar'])
        elif resource[0] == "S":
            cropedImg = rsc[resource]
            pass#cropedImg = gfx.rsc[resource].resize(scales['S_CHCAtributeRsc'])
        
        encodedimg = gfx.PNG_EncodedBase64(cropedImg)
        rsc[resource] = encodedimg

#------------------------------config-------------------------------#
gui.theme(colors['Theme'])

colors['InactiveTab'] = ((gui.theme_element_text_color(), gui.theme_background_color()))
colors['ActiveTab'] = ((gui.theme_button_color()))
colors['TButton'] = ((gui.theme_element_text_color(), gui.theme_background_color()))
colors['PButton'] = (("#eb475a", gui.theme_background_color())) #a21324

setFactors(spacing)
setFactors(scales)
setFontSizing(fonts)

#-----------------------------Resource-----------------------------#

resources = conf.loadPCKData('Data\Resources.pck')
setResources(resources)

#------------------------------Layout------------------------------#
mainLeftColumn  =   [
    {gui.Text("Rol Engine")}
                ]

mainRightColumn =   [
    []
                    ] 

mainLayout  =   [   
    [
        gui.Column(mainLeftColumn),
        gui.Column(mainRightColumn, justification="right")
    ]
                ]

playerInfo = [[
    gui.Column(
        [
            [gui.Image(data = resources['CF_AVATAR'], key="/CLIENT_AVATAR/", pad = ((spacing['W_CHCAvatar'],spacing['W_CHCAvatar']),(spacing['H_CHCAvatar'],0)) , size=scales['S_CHCAvatar'])],

            [gui.FileBrowse("Subir Imagen", key="/CLIENT_AVATARUPLOAD/",    pad = ((spacing['W_CHCAvatarUpload'],0),(0,10)), font = fonts['BFnt'],file_types=(("Png", "*.png"),),enable_events=True)],
            [gui.Input("Nombre",            key="/CLIENT_CHARACTER_NAME/",  pad = ((spacing['W_CHCNAME'],0),0),      font = fonts['IFnt'], size=(20,0), enable_events=True,justification="center")]
        ],pad=(0,0),vertical_alignment="t"),
    
    gui.Column(
        [
            [   gui.Column(
                    [
                        [
                            gui.Text("Edad:",                                       pad = ((0,5),(0,spacing['H_CHCInputSEP'])), font = fonts['FormFnt']),
                            gui.Input("Años",   key = "/CLIENT_CHARACTER_AGE/",     pad = (0,(0,spacing['H_CHCInputSEP'])),     font = fonts['FormFnt'], size=(4,0), enable_events=True,justification="center"),
                        ],
                        [
                            gui.Text("Estatura:",                                   pad = ((0,5),0),       font = fonts['FormFnt']),
                            gui.Input("Metros", key = "/CLIENT_CHARACTER_HEIGHT/",  pad = (0,0),            font = fonts['FormFnt'], size=(6,0), enable_events=True,),
                        ]
                    ],pad=((0,spacing['W_CHCInputSEP']),0),vertical_alignment="t"),
             
                gui.Column(
                    [
                        [
                            gui.Text("Color de piel:",                              pad = ((0,5),(0,spacing['H_CHCInputSEP'])),  font = fonts['FormFnt']),
                            gui.Combo(["Seleccione","Negro", "Blanco kkk"], key="/CLIENT_CHARACTER_RACE/",      readonly=True,    pad = (0,(0,spacing['H_CHCInputSEP'])),       default_value="Seleccione", font=fonts['IFnt'], size=(10,0), enable_events=True,),
                        ],
                        [
                            gui.Text("Genero:",                                     pad = ((0,5),0),       font = fonts['FormFnt']),
                            gui.Combo(["Seleccione","Hombre", "Mujer"],     key="/CLIENT_CHARACTER_GENDER/",    readonly=True,    pad = (0,0),            default_value="Seleccione", font=fonts['IFnt'], size=(10,0), enable_events=True,),
                        ]
                    ],pad=(0,0),vertical_alignment="t"),
            ],
            
            [gui.Text("Descripcion Fisica:", pad = (0,(spacing['H_CHCInputSEP'],20)), font = fonts['FormFnt'])],
            [gui.Multiline("Descripción corta...", key="/CLIENT_CHARACTER_DESCRIPTION/", font=fonts['FormFnt'], no_scrollbar=True, size=(35,scales["R_CHCDesc"]),pad=(0,0))]
            
        ],pad = (0,0),vertical_alignment="t")
    ],
]

playerAttributeInfo = [[
    gui.Column(
        [
            [gui.Image(data=resources['SF_PHOLD_ATTRIBUTE'],pad=(0,0))],
            [gui.Image(data=resources['SF_PHOLD_ATTRIBUTE'],pad=(0,0))],
            [gui.Image(data=resources['SF_PHOLD_ATTRIBUTE'],pad=(0,0))],
            [gui.Image(data=resources['SF_PHOLD_ATTRIBUTE'],pad=(0,0))],
            [gui.Image(data=resources['SF_PHOLD_ATTRIBUTE'],pad=(0,0))],
            [gui.Image(data=resources['SF_PHOLD_ATTRIBUTE'],pad=(0,0))],
            [gui.Image(data=resources['SF_PHOLD_ATTRIBUTE'],pad=(0,0))],
        ],pad = (0,0),vertical_alignment="t"),
    gui.Column([
            [
                gui.Button("00",k="/RND_0/", size = ((4,1)), pad = (0,0),font="Bahnscrift 30", enable_events=False),
                gui.Button("00",k="/RND_1/", size = ((4,1)), pad = (0,0),font="Bahnscrift 30", enable_events=False),
                gui.Button("00",k="/RND_2/", size = ((4,1)), pad = (0,0),font="Bahnscrift 30", enable_events=False),
                gui.Button("00",k="/RND_3/", size = ((4,1)), pad = (0,0),font="Bahnscrift 30", enable_events=False),
                gui.Button("00",k="/RND_4/", size = ((4,1)), pad = (0,0),font="Bahnscrift 30", enable_events=False),
            ],
            [
                gui.Button("00",k="/RND_5/", size = ((4,1)), pad = (0,0),font="Bahnscrift 30", enable_events=False),
                gui.Button("00",k="/RND_6/", size = ((4,1)), pad = (0,0),font="Bahnscrift 30", enable_events=False),
                gui.Button("00",k="/RND_7/", size = ((4,1)), pad = (0,0),font="Bahnscrift 30", enable_events=False),
                gui.Button("00",k="/RND_8/", size = ((4,1)), pad = (0,0),font="Bahnscrift 30", enable_events=False),
                gui.Button("00",k="/RND_9/", size = ((4,1)), pad = (0,0),font="Bahnscrift 30", enable_events=False),
            ],
            [gui.Button("Roll",k="/ROLL/")]
        ],pad = (0,0),vertical_alignment="t")
    ]
]


characterCreation   =   [
    [
        gui.Button("Basica",    key="/CLIENT_BASICINFO/",       pad=((spacing['W_CHCMarGins'],0),0),  font = fonts['TabFnt'], border_width = 0, button_color = colors['ActiveTab']),
        gui.Button("Atributos", key="/CLIENT_ATTRIBUTEINFO/",   pad=(0,0),                          font = fonts['TabFnt'], border_width = 0, button_color = colors['InactiveTab']),
        gui.Text("Creacion de personajes",                      pad=((spacing['W_CHCCenterTittle'],0),0),font = fonts['TFnt']),
    ],
    [   gui.Text("¿Quién será nuestro heroe?:", pad=((spacing['W_CHCMarGins'],0),(spacing['H_CHCMotd'],0)), font=fonts['STFnt'])],
    
    [
        gui.Column(playerInfo,          key="/PLAYERINFO_LAYOUT/",      pad = (0,0), visible = True),
        gui.Column(playerAttributeInfo, key="/PLAYERATTINFO_LAYOUT/",   pad = (0,0), visible = False)
    ],
    
    [
        gui.Button("Volver",    key="/BACKMAIN/",           pad = ((spacing['W_Controls'],10),0),    font = fonts['CtrlFnt'], border_width = 0, button_color = colors['TButton'], mouseover_colors = colors["PButton"]),
        gui.Button("Siguiente", key="/NEXTHABILITIES/",     pad = ((0,0),0),        font = fonts['CtrlFnt'], border_width = 0, button_color = colors['TButton'], mouseover_colors = colors["PButton"], disabled = True),

    ],
]