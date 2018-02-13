from django.shortcuts import render
from .models import UploadForm, Upload
from django.http import HttpResponse
from .models import Photo
from .color_feature import *
from .shape_feature import *
from .forms import picForm
import time

# Create your views here.
def home(request) :
    context = locals()
    template = 'index.html'
    return render(request, template, context)

def color(request):
    # make stopwatch to count the time that has passed
    start = time.time()
    time.clock()
    title = "Search Image"
    img = UploadForm(request.POST, request.FILES or None)
    position = "first"
    imageUrl = None
    imageName = None
    confirm_message = "Image Searching"
    filteredCS = ''
    notif = None
    query = None

    if img.is_valid():
        autoDelete()
        img.save()
        title = "Searching...."
        position = "second"
        images = Upload.objects.last()
        url = settings.STATIC_ONLY + images.pic.url
        query = images.pic.name
        imageOpen = Image.open(url)
        cosSimilarity = matchColorQuery(imageOpen)
        filteredCS = delZeroValue(cosSimilarity)
        image = sortTheImage(filteredCS)
        imageUrl = getUrlImage(image)
        imageName = getNameImage(image)
        #sort the cosine result
        filteredCS = sorted(filteredCS, reverse=True)
        confirm_message = "Search Based on Color"
        #check if there are any results or not
        if len(filteredCS) == 0 :
            notif = "Sorry, there are not any results from your query"
    # stop the counting of stopwatch
    elapsed = time.time() - start
    elapsed = round(elapsed, 2)
    time.sleep(1)
    context = {
        'title' : title ,
        'form': img,
        'result' : imageUrl,
        'confirm_message' : confirm_message,
        'similar' : filteredCS,
        'name' : imageName,
        'position' : position,
        'time' : elapsed,
        'notif' : notif,
        'query' : query
    }
    return render(request, 'home.html', context)

def shape(request):
    # make stopwatch to count the time that has passed
    start = time.time()
    time.clock()
    title = "Search Image"
    img = UploadForm(request.POST, request.FILES or None)
    position = "first"
    imageUrl = None
    imageName = None
    confirm_message = "Image Searching"
    filteredCS = ''
    notif = None
    query = None

    if img.is_valid():
        autoDelete()
        img.save()
        title = "Searching...."
        position = "second"
        imgDatabase = Photo.objects.all()
        images = Upload.objects.last()
        url = settings.STATIC_ONLY + images.pic.url
        query = images.pic.name
        cosSimilarity = fourierProcess(url, imgDatabase)
        filteredCS = delZeroValue(cosSimilarity)
        image = sortTheImage(filteredCS)
        imageUrl = getUrlImage(image)
        imageName = getNameImage(image)
        #sort the cosine result
        filteredCS = sorted(filteredCS, reverse=True)
        confirm_message = "Search Based on Shape"
        # check if there are any results or not
        if len(filteredCS) == 0:
            notif = "Sorry, there are not any results from your query"

    # stop the counting of stopwatch
    elapsed = time.time() - start
    elapsed = round(elapsed, 2)
    time.sleep(1)
    context = {
        'title' : title ,
        'form': img,
        'result' : imageUrl,
        'confirm_message' : confirm_message,
        'similar' : filteredCS,
        'name' : imageName,
        'position' : position,
        'time' : elapsed,
        'notif' : notif,
        'query': query
    }
    return render(request, 'home.html', context)

def colorByExample(request):
    # make stopwatch to count the time that has passed
    start = time.time()
    time.clock()
    title = 'Search Image'
    form = picForm(request.POST, request.FILES or None)
    position = "first"
    imageUrl = None
    imageName = None
    confirm_message = "Image Searching"
    filteredCS = ''
    notif = None
    query = None

    if form.is_valid():
        name = form.cleaned_data['name']
        title = "Searching...."
        position = "second"
        url = settings.STATIC_DIR + "/"+ name
        query = name
        imageOpen = Image.open(url)
        cosSimilarity = matchColorQuery(imageOpen)
        filteredCS = delZeroValue(cosSimilarity)
        image = sortTheImage(filteredCS)
        imageUrl = getUrlImage(image)
        imageName = getNameImage(image)
        # sort the cosine result
        filteredCS = sorted(filteredCS, reverse=True)
        confirm_message = "Search Based on Color"
        # check if there are any results or not
        if len(filteredCS) == 0:
            notif = "Sorry, there are not any results from your query"
        # stop the counting of stopwatch
    elapsed = time.time() - start
    elapsed = round(elapsed, 2)
    time.sleep(1)
    context = {
        'title': title,
        'form': form,
        'result': imageUrl,
        'confirm_message': confirm_message,
        'similar': filteredCS,
        'name': imageName,
        'position': position,
        'time': elapsed,
        'notif': notif,
        'query': query
    }
    return render(request, 'fileInput.html', context)

def shapeByExample(request):
    # make stopwatch to count the time that has passed
    start = time.time()
    time.clock()
    title = 'Search Image'
    form = picForm(request.POST, request.FILES or None)
    position = "first"
    imageUrl = None
    imageName = None
    confirm_message = "Image Searching"
    filteredCS = ''
    notif = None
    query = None

    if form.is_valid():
        name = form.cleaned_data['name']
        title = "Searching...."
        position = "second"
        imgDatabase = Photo.objects.all()
        url = settings.STATIC_DIR + "/"+ name
        query = name
        cosSimilarity = fourierProcess(url, imgDatabase)
        filteredCS = delZeroValue(cosSimilarity)
        image = sortTheImage(filteredCS)
        imageUrl = getUrlImage(image)
        imageName = getNameImage(image)
        # sort the cosine result
        filteredCS = sorted(filteredCS, reverse=True)
        confirm_message = "Search Based on Shape"
        # check if there are any results or not
        if len(filteredCS) == 0:
            notif = "Sorry, there are not any results from your query"

        # stop the counting of stopwatch
    elapsed = time.time() - start
    elapsed = round(elapsed, 2)
    time.sleep(1)
    context = {
        'title': title,
        'form': form,
        'result': imageUrl,
        'confirm_message': confirm_message,
        'similar': filteredCS,
        'name': imageName,
        'position': position,
        'time': elapsed,
        'notif': notif,
        'query': query
    }
    return render(request, 'fileInput.html', context)

def autoDelete():
    query = Upload.objects.all()
    query.delete()
    return HttpResponse("Deleted!")

def matchColorQuery(img) :
    # get array of consisting pixel in photo/picture in database
    all_photo = Photo.objects.all()
    sumPhoto = len(all_photo)
    data = getArrayfromPic(all_photo)
    # clustering the color into 4 bins
    hist = makeHisto(data)
    # counting the pixel in image
    pixCount = labelFromHisto(hist)
    # find cosinus similarity between image inputted from user and image in database, then sort it in descending
    res = changeImageToHistogram(img)
    resultImage = cosineInputwithDatabase(sumPhoto, pixCount, res)
    return resultImage

def sortTheImage(index):
    indexForViewing = np.zeros(shape=len(index)).tolist()
    for ind, item in enumerate(indexForViewing) :
        indexForViewing[ind] = ind
    sortFfile = [indexForViewing for _, indexForViewing in sorted(zip(index, indexForViewing), reverse=True)]

    return sortFfile

def getUrlImage(file) :
    imgDatabase = Photo.objects.all()
    url = np.zeros(shape=len(file)).tolist()
    for ind, img in enumerate(file):
        url[ind] = imgDatabase[img].pic.url

    return url

def getNameImage(file):
    imgDatabase = Photo.objects.all()
    name = np.zeros(shape=len(file)).tolist()
    for ind, img in enumerate(file):
        name[ind] = imgDatabase[img].quote

    return name

def delZeroValue (cos_arr):
    sum = len(cos_arr)
    for i in range(sum - 1, -1, -1):
        if cos_arr[i] == 0:
            del cos_arr[i]

    return cos_arr







