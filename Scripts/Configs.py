#--------------------------Library Import--------------------------#
import json
from PySimpleGUI import Window
#--------------------------Functions list--------------------------#
width, height = Window.get_screen_size()
defaults = {
    'WindowedRes' : (round(width*0.75), round(height*0.75)),
    }
    
def DetectConfigs():
    """ 
    Definition:
    ------------
    Detects if there is a config.json file in Data folder if not it creates it.
    
    Returns:
    -------------
    Bool value if there is or not a config file.
    """
    try:
        data = open(".\data\Configs.json","r")
        data.close()
        return True
    except FileNotFoundError:
        data = open(".\data\configs.json","x")
        data.close()
        return False

def Defaults():
    """ 
    Definition:
    ------------
    Sets the defaults of the configuration file.
    """
    config = defaults
    
    data = open(".\data\configs.json","w")
    data.write(json.dumps(config))
    data.close()

def GetConfigs():
    """ 
    Definition:
    ------------
    Reads configs.json and returns the contents as an dictionary
    
    Returns:
    -------------
    <Dict> object with the configurations.
    """
    data = open(".\data\configs.json","r")
    config = json.loads(data.read())
    # Some Bug preventing code
    data.close()
    if config['WindowedRes'] != [round(width*0.75), round(height*0.75)]:
        config['WindowedRes'] = [round(width*0.75), round(height*0.75)]
        print("Resolucion nueva detectada")
        SaveConfigs(config)
    return config

def SaveConfigs(config):
    """ 
    Definition:
    ------------
    Saves the configuration made in configs.json
    
    Parameters:
    -----------
    config <Dict>
        The configuration dictionary object.
    """
    data = open(".\data\configs.json","w")
    data.write(json.dumps(config))
    data.close()
    