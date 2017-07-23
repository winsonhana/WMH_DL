import os, re, csv, collections
import numpy as np
import matplotlib.pyplot as plt
import openslide
import scipy.ndimage as ndimage
import PIL

def GetImage(path,level):
    oslideimg = openslide.OpenSlide(path)
    assert (level < oslideimg.level_count), "level > level_count"
    img = oslideimg.read_region((0,0),level%oslideimg.level_count,oslideimg.level_dimensions[level])
    attr = [(oslideimg.level_dimensions[ll],oslideimg.level_downsamples[ll]) for ll in range(0,oslideimg.level_count)]
    return img, attr


def CropImageRatio(image_in,w_min,h_min,w_max,h_max):
    wd, hd = image_in.size
    w1, w2 = int(w_min*wd + 0.5), int(w_max*wd + 0.5)
    h1, h2 = int(h_min*hd + 0.5), int(h_max*hd + 0.5)
    return image_in.crop((w1,h1,w2,h2))
    
img, attr = GetImage('./Tumor_001_Mask.tif',2)
print(type(img))
print(img.shape)
#PIL.Image.Image.save()