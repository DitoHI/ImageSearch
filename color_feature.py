from django.conf import settings
from PIL import Image
from sklearn.utils import shuffle
import numpy as np
import copy as cp
from math import sqrt

bins = 4 # define the bins for image
maxHex = 256
maxSample = 1000
maxBasis = 3

def getArrayfromPic(all_photo) :
    newData = np.zeros(shape=(len(all_photo), maxSample, maxBasis))
    start = 0 #counter from 0 until end
    for photo in all_photo:
        url = settings.STATIC_ONLY + photo.pic.url
        img = Image.open(url)
        temp =  np.array(img, dtype=np.float64)
        w, h, d = tuple(temp.shape)
        # change the shape of any List to shape(height, weight, maxBasis)
        if d > maxBasis : # if the picture already 'RGB' the basis must be 3 otherwise more than 3
            img.load()
            img = Image.new("RGB", img.size, (255, 255, 255)) # so this code try to reduce the basis to 3 in cases the picture is RGBA
        data = np.array(img, dtype=np.float64)
        # Make the shape into two dimensional and resample
        w, h, d = tuple(data.shape)
        image_array = np.reshape(data, (w * h, d))
        image_array_sample = shuffle(image_array, random_state=0)[:maxSample]
        newData[start] = np.asarray(image_array_sample)
        start += 1
    # return value : array consist all of pixel in picture
    return np.asarray(newData).tolist()

def makeHisto(pic):
    res = maxHex // bins
    global clust
    clust = np.zeros(shape=bins).tolist()
    a = 0
    resCopy = cp.deepcopy(res)
    for i in range(resCopy,maxHex,res):
        clust[a] = i
        a += 1
    start = 0
    for loop1 in range(0, len(pic)):  # looping for element in dimension one
        for loop2 in range(0, len(pic[loop1])):  # looping for element in dimension two
            for loop3 in range(0, len(pic[loop1][loop2])):  # looping for element in dimension three
                container = pic[loop1][loop2][loop3]
                for stop in clust:
                    if container <= stop:
                        pic[loop1][loop2][loop3] = start
                        break
                    else:
                        pic[loop1][loop2][loop3] = start
                    start += 1
                start = 0

    return pic

def labelFromHisto(res) :
    #initialize the pallete of color based on bins
    global temp # turn it into global to make its value accessible outside the function
    temp = np.zeros(shape=maxHex // bins).tolist()
    start = 0
    for i in range(0, bins):
        for j in range(0, bins):
            for k in range(0, bins):
                temp[start] = [i, j, k]
                start += 1

    #initialize the pixel count for each PICTURE's pixel and assign the sum of the count
    pixelCount = np.zeros(shape=(len(res), len(temp))).tolist()
    for loop1 in range(0, len(res)):
        for loop2 in res[loop1] :
            index = temp.index(loop2)
            pixelCount[loop1][index] += 1

    return pixelCount

def cosineInputwithDatabase(iter, hist, src) :
    coba = cp.deepcopy(src)
    cos = np.zeros(shape=iter).tolist()
    for i in range(0, iter):
        dpaa = 0
        dpab = 0
        dpbb = 0
        for j in range(0, len(hist[i])):
            simpan = hist[i][j] * hist[i][j]
            dpaa += simpan
            simpan = coba[j] * coba[j]
            dpbb += simpan
            simpan = hist[i][j] * coba[j]
            dpab += simpan

        lpab = sqrt(dpaa) * sqrt(dpbb)
        cos[i] = dpab / lpab
        cos[i] =round(cos[i], 5)

    return cos

def changeImageToHistogram(source) :
    data = np.array(source, dtype=np.float64)
    w, h, d = tuple(data.shape)
    imageArr = np.reshape(data, (w * h, d))
    imageSample = shuffle(imageArr, random_state=0)[:1000]
    imageList = np.asarray(imageSample).tolist()
    start = 0
    for loop1 in range(0, len(imageList)):  # looping for element in dimension one
        for loop2 in range(0, len(imageList[loop1])):  # looping for element in dimension two
            container = imageList[loop1][loop2]
            for stop in clust:
                if container <= stop:
                    imageList[loop1][loop2] = start
                    break
                else:
                    imageList[loop1][loop2] = start
                start += 1
            start = 0

    sumPixel = np.zeros(shape=(len(temp))).tolist()
    for loop in range(0, len(imageList)):
        index = temp.index(imageList[loop])
        sumPixel[index] += 1

    return sumPixel









