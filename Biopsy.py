#import os, re, csv, collections
#import numpy as np
#import matplotlib.pyplot as plt
import openslide
#import scipy.ndimage as ndimage
#import PIL

def GetImage(path,level):
    oslideimg = openslide.OpenSlide(path)
    print(type(oslideimg))
    print(oslideimg.dimensions)
    print(oslideimg.level_dimensions[0])
    print(oslideimg.level_dimensions[1])
    print(oslideimg.level_dimensions[2])
    print(oslideimg.level_dimensions[3])
    print(oslideimg.level_count)
    print(level%oslideimg.level_count)
    assert (level < oslideimg.level_count), "level > level_count"
    #img = oslideimg.read_region((0,0),level%oslideimg.level_count,oslideimg.level_dimensions[level])
    img = oslideimg.read_region((25000,40000),1,(7000,7000 ))
    attr = [(oslideimg.level_dimensions[ll],oslideimg.level_downsamples[ll]) for ll in range(0,oslideimg.level_count)]
    return img, attr


def CropImageRatio(image_in,w_min,h_min,w_max,h_max):
    wd, hd = image_in.size
    w1, w2 = int(w_min*wd + 0.5), int(w_max*wd + 0.5)
    h1, h2 = int(h_min*hd + 0.5), int(h_max*hd + 0.5)
    return image_in.crop((w1,h1,w2,h2))


path = "/home/data/CAMELYON16/TrainingData/Train_Tumor/Tumor_054.tif"
#path = "/home/data/CAMELYON16/TrainingData/Ground_Truth/Mask/Tumor_002_Mask.tif"
#img, attr = GetImage('./Tumor_002_Mask.tif',1) # THROW ERROR INTEGER OVERFLOW
img, attr = GetImage(path,6)
print(type(img))
print(img.height)
print(img.width)
img.save('Tumor054_1.tif')


path = "/home/data/CAMELYON16/TrainingData/Ground_Truth/Mask/Tumor_054_Mask.tif"
img, attr = GetImage(path,6)
print(type(img))
print(img.height)
print(img.width)
img.save('Mask054_1.tif')


# LEGEND
"""
<class 'openslide.OpenSlide'>
(97792, 221184)
(97792, 221184)
(49152, 110592)
(24576, 55296)
(12288, 27648)
<class 'PIL.Image.Image'>
3584
1536


6 -- 
3456
1528

2 -- ERROR

3 -- 
27648
12224


"""