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
    TODO : For client
        TODO : Character Creation Assistant
            TODO : Basic Info (work in progress)
            TODO : Atribbutte info  
    TODO : For master
        TODO : Character Display 
        TODO : Character panel magnagement
        
'''

#--------------------------Library Import--------------------------#
import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import Button
import Configs as conf


#---------------------------Variable Def---------------------------#

if conf.DetectConfigs():
    configs = conf.GetConfigs()
else:
    conf.Defaults()
    configs = conf.GetConfigs()

# Color and font Dicts

colors = {
    'Theme' : "Light Brown 13", # Internal Theme of Pysimplegui
    'ButtonColor' : None, #Set the configs for Button color (Without Background)
    }
fonts = {
    'Font' : "BahnschriftLight ", #The family of the font
    'TFnt' : 7.4,
    'BFnt' : 4.2,
    'TabFnt' : 4.4,
    'SbmFnt' : 0,
    }

# This last one is very special, the spacings have codes and the values are listed in the pdf

spacing = {
    'SPW_CHC_MG' : 1.5, # Margins of the row
    'SPW_CHC_1' : 45, # The central between The buttons and the tittle
}

#-----------------------------Function------------------------------#
def setSpacings(SPCs):
    '''
    Definition:
    ------------
    Takes all the percentages put in the spacing dict and rewrittes every value
    converting them to pixel space related to the actual window size
    
    '''
    widthFactor = configs["WindowedRes"][0]/100
    heightFactor = configs["WindowedRes"][1]/100
    for Space in SPCs:
        SPCs[Space] *= widthFactor

def setFontSizing(FNTs):
    widthFactor = configs["WindowedRes"][1]/100
    for size in FNTs:
        if size != 'Font':
            value = 0.6697 * (FNTs[size]*widthFactor) - 3.1135 # That comes from a linear regression of the Pt vs Px values
            FNTs[size] = FNTs["Font"] + str(round(value))



#------------------------------config-------------------------------#
gui.theme(colors['Theme'])
colors['ButtonColor'] = ((gui.theme_element_text_color(), gui.theme_background_color()))
setSpacings(spacing)
setFontSizing(fonts)

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

basicInfoClient = [[
    gui.Column(
        [
            [gui.Button()],

            [gui.FileBrowse("Subir Imagen", key="/CLIENT_AVATARUPLOAD/")],
            [gui.Input("Nombre", key="/CLIENT_CHARACTERNAME/", )]
        ],pad=(0,0)),
    
    gui.Column(
        [
            [
                gui.Text("Edad:",),
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
        ],pad=(0,0))
    ],
]

characterCreation   =   [
    [
        gui.Button("Basica",                key="/CLIENT_BASICINFO/",       pad=((spacing['SPW_CHC_MG'],0),0),                      font = fonts['BFnt'], border_width = 0, button_color = colors['ButtonColor']),
        gui.Button("Atributos",             key="/CLIENT_ATTRIBUTEINFO/",   pad=(0,0),                                              font = fonts['BFnt'], border_width = 0, button_color = colors['ButtonColor']),
        gui.Text("Creacion de personajes",  key="/CLIENT_CHARCRTITTLE/",    pad=((spacing['SPW_CHC_1'],25),0),   font = fonts['TFnt']),
    ],
    
    [
        gui.Column(basicInfoClient, key="/BASICINFO_LAYOUT/", pad=(0,0))
    ],
    
    [
        gui.Button("Volver",    key="/BACKMAIN/",       font = fonts['BFnt'], border_width = 0, button_color = colors['ButtonColor']),
        gui.Button("Siguiente", key="/NEXTHABILITIES/", font = fonts['BFnt'], border_width = 0, button_color = colors['ButtonColor']),

    ],
]