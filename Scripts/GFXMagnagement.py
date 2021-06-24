#----------------------------TO DO list--------------------------#

"""
[DONE] : Crop in a circle a image
TODO : Save a image
TODO : Autosize a image to meet certain resolution.

"""
#--------------------------Library Import--------------------------#
from PIL import Image, ImageDraw
import numpy as np

#We have to come back here to do some changes in the algorithm to implement this in the layout

data = Image.open(".\TestAssets\Pillow Test.png").convert("RGB").resize((500,500), Image.HAMMING)
npData = np.array(data)
height, weight = data.size

alpha = Image.new("L", data.size, 0)
draw = ImageDraw.Draw(alpha)

draw.pieslice([0,0,height,weight],0,360,fill=255)

npAlpha = np.array(alpha)
npData = np.dstack((npData,npAlpha))

finalimg = Image.fromarray(npData)

finalimg.show()
