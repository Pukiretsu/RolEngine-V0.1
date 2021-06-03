"""
Definition
------------------
This module defines the layouts of the app
please refer to PySimpleGUI for futher information 
about layouts

"""
#----------------------------TO DO list--------------------------#
'''
TODO : Start prototyping the UX
'''
#--------------------------Library Import--------------------------#
import PySimpleGUI as gui

mainLayout  =   [   
                    #[gui.Titlebar(title="Rol Engine launcher",key='/Tittle/')],
                    
                    [
                        gui.Text("Hora de ponernos en pantalla completa :)\n",key='/textoPrueba/'),
                        gui.Button(key="/Fullscreen/", button_text="Pantalla completa")
                    ],
                    [gui.Button(key="/exit/",button_text="Salir")]
                ]

