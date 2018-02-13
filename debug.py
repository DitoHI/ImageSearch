from django.shortcuts import render
from PIL import Image
from django.conf import settings
import scipy.misc
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

url = Image.open("C:/Users/Kudo/Pictures/Tugas/Semester 7 - Teknologi Web/2.jpg")
url = settings.STATIC_DIR + "/spectral/gb1.GIF"
url = scipy.misc.imresize(url, (300,300))
rgb = rgb2gray(url)

print("url: ", url)
print("rgn: ", rgb)







