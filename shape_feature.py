from django.conf import settings
from PIL import Image
import scipy.misc

import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def fourierProcess(url, imgDb):
    imgUser = Image.open(url)
    imgUser = scipy.misc.imresize(imgUser, (300,300))
    imgUser = rgb2gray(imgUser)
    four1 = np.fft.fft2(imgUser)
    fshift1 = np.fft.fftshift(four1)
    fshift1 = fshift1.real
    w, h = tuple(fshift1.shape)
    fshift1 = np.reshape(fshift1, (w * h)).tolist()

    cosSimilar = np.zeros(shape=len(imgDb)).tolist()
    for ind, dbItems in enumerate(imgDb):
        imgDbUrl = settings.STATIC_ONLY + dbItems.pic.url
        img2 = Image.open(imgDbUrl)
        img2 = scipy.misc.imresize(img2, (300,300))
        img2 = rgb2gray(img2)
        four2 = np.fft.fft2(img2)
        fshift2 = np.fft.fftshift(four2)
        fshift2 = fshift2.real
        w, h = tuple(fshift2.shape)
        fshift2 = np.reshape(fshift2, (w * h)).tolist()
        cosSimilar[ind] = cos(fshift1, fshift2)
        cosSimilar[ind] = round(cosSimilar[ind], 5)

    return cosSimilar

def cos(v1, v2):
    return np.dot(v1, v2) / (np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2)))