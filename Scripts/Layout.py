from PySimpleGUI import Text,Button
"""
Definition
------------------
This module defines the layouts of the app
please refer to PySimpleGUI for futher information 
about layouts

"""
# TODO : Start prototyping the UX
mainLayout  =   [   
                    [
                        Text("Hora de ponernos en pantalla completa :)",key='/textoPrueba/'),
                        Button(key="/Fullscreen/", button_text="Pantalla completa")
                    ],
                    [Button(key="/exit/",button_text="Salir")]
                ]
