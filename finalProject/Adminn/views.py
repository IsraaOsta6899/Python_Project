from pyexpat import model
from django.shortcuts import render,HttpResponse,redirect
from Adminn import models

# Create your views here.
def index(request):
    return render(request , 'editAnimal.html')
def requestPage(request):
    context={
        'requests':models.getAllRequests(request.POST)
    }
    return render(request ,'requests.html',context)
def accept(request,animalid):
                models.accept(request.POST,animalid)
                return redirect('/requestPage')
def reject(request,animalid):
    
                models.reject(request.POST,animalid)
                return redirect('/requestPage')

def edit_info(request,animal1_id):
    models.edit_info1(request.POST,animal1_id)
    return redirect('/mainPage')
def deleteAnimal(request, animalid):
    models.deleteAnimal(animalid)
    return redirect('/mainPage')
