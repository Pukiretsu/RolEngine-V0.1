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
from tkinter import font
import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import Button, Col, Column
import Configs as conf
#-----------------------------Resource-----------------------------#

Data = open("placeholder3.png", "rb")
PlaceHolder = Data.read()
Data.close()


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
    # Text fonts
    'TFnt' : 7.4, # Tittles 
    'STFnt' : 5, # SubTittle 
    'IFnt' : 5, #Input enter
    'FormFnt' : 6, # Age input 
    # Element fonts
    'BFnt' : 3.5, # Buttons 
    'CtrlFnt' : 4.2, # Proced and Back button 
    'TabFnt' : 4.4, # Button type Tab 
    }

# This last one is very special, the spacings have codes and the values are listed in the pdf

spacing = {
    'SPW_CHC_MG' : 1.5, # Margins of the row
    'SPW_CHC_1,1' : 44, # The central between The buttons and the tittle
    'SPH_CHC_2,1' : 0.5, # Over the
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
            [gui.Button("",key="PH", disabled=False, pad = ((50,60),(20,0)), border_width = 0, image_data = PlaceHolder, image_size=(500,500),button_color = colors['ButtonColor'])],

            [gui.FileBrowse("Subir Imagen", key="/CLIENT_AVATARUPLOAD/",    pad = ((231,0),(0,10)), font = fonts['BFnt'])],
            [gui.Input("Nombre",            key="/CLIENT_CHARACTER_NAME/",  pad = ((118,0),0),      font = fonts['IFnt'], size=(20,0), justification="center")]
        ],pad=(0,0),vertical_alignment="t"),
    
    gui.Column(
        [
            [   gui.Column(
                    [
                        [
                            gui.Text("Edad:",                                       pad = ((0,10),(0,40)),  font = fonts['FormFnt']),
                            gui.Input("Años", key = "/CLIENT_CHARACTER_AGE/",       pad = (0,(0,40)),       font = fonts['FormFnt'], size=(4,0), justification="center"),
                        ],
                        [
                            gui.Text("Estatura:",                                   pad = ((0,10),0),       font = fonts['FormFnt']),
                            gui.Input("Metros", key = "/CLIENT_CHARACTER_HEIGHT/",  pad = (0,0),            font = fonts['FormFnt'], size=(6,0)),
                        ]
                    ],pad=((0,30),0),vertical_alignment="t"),
             
                gui.Column(
                    [
                        [
                            gui.Text("Color de piel:",                              pad = ((0,10),(0,40)),  font = fonts['FormFnt']),
                            gui.Combo(["Seleccione","Negro", "Blanco kkk"], key="/CLIENT_CHARACTER_RACE/",      pad = (0,(0,40)),       default_value="Seleccione", font=fonts['IFnt'], size=(10,0)),
                        ],
                        [
                            gui.Text("Genero:",                                     pad = ((0,10),0),       font = fonts['FormFnt']),
                            gui.Combo(["Seleccione","Hombre", "Mujer"],     key="/CLIENT_CHARACTER_GENDER/",    pad = (0,0),            default_value="Seleccione", font=fonts['IFnt'], size=(10,0)),
                        ]
                    ],pad=(0,0),vertical_alignment="t"),
            ],
            
            [



            ],
            
            [gui.Text("Descripcion General:", pad = (0,(40,20)), font = fonts['FormFnt'])],
            [gui.Multiline("Descripción corta...", key="/CLIENT_CHARACTER_DESCRIPTION/", font=fonts['FormFnt'], no_scrollbar=True, size=(35,8))]
            
        ],pad=(0,0),vertical_alignment="t")
    ],
]

characterCreation   =   [
    [
        gui.Button("Basica",    key="/CLIENT_BASICINFO/",       pad=((spacing['SPW_CHC_MG'],0),0),  font = fonts['TabFnt'], border_width = 0),
        gui.Button("Atributos", key="/CLIENT_ATTRIBUTEINFO/",   pad=(0,0),                          font = fonts['TabFnt'], border_width = 0, button_color = colors['ButtonColor']),
        gui.Text("Creacion de personajes",                      pad=((spacing['SPW_CHC_1,1'],25),0),font = fonts['TFnt']),
    ],
    [   gui.Text("¿Quién será nuestro heroe?:", pad=((spacing['SPW_CHC_MG'],0),(spacing['SPH_CHC_2,1'],0)), font=fonts['STFnt'])],
    
    [
        gui.Column(basicInfoClient, key="/BASICINFO_LAYOUT/", pad=(0,0))
    ],
    
    [
        gui.Button("Volver",    key="/BACKMAIN/",           pad = ((1172,10),0), font = fonts['CtrlFnt'], border_width = 0, button_color = colors['ButtonColor']),
        gui.Button("Siguiente", key="/NEXTHABILITIES/",     pad = ((0,0),0), font = fonts['CtrlFnt'], border_width = 0, button_color = colors['ButtonColor']),

    ],
]