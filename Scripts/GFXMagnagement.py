'''
USE
-----
This script is used to manage all the image assets in the game
'''
#----------------------------TO DO list--------------------------#

"""
[DONE] : Crop in a circle a image
[DONE] : Save a image
[DONE] : Autosize a image to meet certain resolution.

"""
#--------------------------Library Import--------------------------#
from PIL import Image, ImageDraw
import io
import numpy as np
import Configs as cfg
import base64
import pickle as pck

def PNGCircleCrop(dir, imgobj, size):
    '''
    Definition
    -----------
    This funtion takes a png file, rezises it and crops it into a circular mask
    returning a PIL image object.
    
    Args
    -----------
    dir <str>:
        A string with the path of the png file.
    imgobj <PIL.Image Object>:
        A prexisting PIL image object.
    size <tuple> (width, height):
        A tuple with the size in px of the output image.
    
    Returns
    -------------
    image <object>
        The Function returns a PIL image object that represents crop input image. 
    '''
    # Reading the image
    if dir != None:
        data = Image.open(dir).convert("RGB").resize(size, Image.HAMMING)
    else:
        data = imgobj.resize(size, Image.HAMMING)
    
    # Creating an array from the data 
    npData = np.array(data)
    height, weight = data.size # Storing the size property 

    # Creating a mask 
    alpha = Image.new("L", data.size, 0)
    
    # Drawing the mask
    draw = ImageDraw.Draw(alpha)

    # Seting the circle
    draw.pieslice([0,0,height,weight],0,360,fill=255)

    # From a array merging the 2 sets of data
    npAlpha = np.array(alpha)
    npData = np.dstack((npData,npAlpha))

    # Output Resut image
    finalimg = Image.fromarray(npData)

    return finalimg

def PNG_EncodedBase64(img):
    '''
    Definition
    -----------
    Encodes a Pil image object into a Base64 encoded PNG
    
    Args
    ---------
    img <Pil.image.object>
        The PIL image object to encode
    
    Returns
    --------
    Imgbase64 <byte>
        A PNG encoded as Base64 bytes
    '''
    # Creating a BytesIO object to wrap the image into the buffer
    imageMemory = io.BytesIO()
    
    # Saving the image as png
    img.save(imageMemory, format="PNG")
    
    # Repositioning the pointer
    imageMemory.seek(0)
    
    # Reading and encoding as Base64 bytes
    imageBytes = imageMemory.read()
    Imgbase64 = base64.b64encode(imageBytes)
    return Imgbase64

def storeImg(dir, diction, key):
    data = Image.open(dir).convert("RGB")
    diction[key] = data


#Rsc = {cfg.loadPCKData("Data\Resources.pck")}
""" Rsc = {}

storeImg("Data\Assets\PlaceHolder.png",Rsc,'CF_AVATAR')
storeImg("TestAssets\ATTPLACEHOLDER.png",Rsc,'SF_PHOLD_ATTRIBUTE')
cfg.savePCKData(Rsc,"Data\Resources.pck")

print(Rsc) """