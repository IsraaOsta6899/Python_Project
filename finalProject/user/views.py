from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'login.html')
def openregisterpage(request):
    return render(request,'registration.html')
def openMainPage(request):
    return render (request, 'mainPage.html')

def showAllAnimals(request):
    return render (request, 'mainPage.html')

def addAnimalPage(request):
    return render (request, 'add_animal.html')

def allCategories(request):
    return render (request, 'all_catogries.html')

def aboutUs(request):
    return render (request, 'aboutUs.html')
