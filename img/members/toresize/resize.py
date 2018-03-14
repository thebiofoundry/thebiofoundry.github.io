#!/usr/bin/env python3
#resize all images int a current working directory to #fit a300x 300 square,



import os 
from PIL import Image
SQUARE_FIT_SIZE = 300


os.makedirs('sized',exist_ok=True)
#loop over all files in the working directory

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('jpg')):
        continue
    im=Image.open(filename)
    width,height = im.size
    
    height = int((SQUARE_FIT_SIZE/width)*height)
    width = SQUARE_FIT_SIZE
    
    # height= 300
    # width = 200
        #resizes the photo
        # left top right bot
    print ( 'REsizing %s...' %(filename))
    im = im.resize((width,height), Image.ANTIALIAS)
     # im = im.crop((2000,0,4000,2667)) #for landscape A6000
    # im = im.crop((0,0,4000,5333)) # for portrait A6000 
    im.save(os.path.join('sized', filename))