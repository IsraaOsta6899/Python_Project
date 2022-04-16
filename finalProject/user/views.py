from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect

from user import models
from user.models import User,Category,Animal

# Create your views here.
def index(request):
    return render(request,'login.html')
def openregisterpage(request):
    return render(request,'registration.html')
def openMainPage(request):
    context={
        'user': User.objects.get(id=5)
    }
    return render (request, 'mainPage.html')

def showAllAnimals(request):
    return render (request, 'mainPage.html')

def addAnimalPage(request):

    context={
        'categories': Category.objects.all()
    }
    if request.method=='POST':
        animal = Animal()
        animal.animal_name=request.POST['pet_name']
        animal.age=request.POST['pet_age']
        animal.description=request.POST['pet_description']
        animal.price=request.POST['pet_price']
        c=Category.objects.get(id=request.POST['catgs'])
        animal.category=c
        animal.isDelete=False
        animal.isAccepted=False
        user=User.objects.get(id=1)
        animal.added_by=user
        if len(request.FILES )!=0 :
            animal.image=request.FILES['upload']
        animal.save()
        return redirect('/mainPage')
    return render (request, 'add_animal.html', context)

def allCategories(request):
    return render (request, 'all_catogries.html')

def aboutUs(request):
    return render (request, 'aboutUs.html')
def rigister(request):
    models.rigister(request.POST)
    return redirect('/')

def login(request):
    # errors2 = User.objects.login_validator(request.POST)
        
    # if len(errors2) > 0:
    #     context={
    #         'flag':1
    #     }
       
    #     for key, value in errors2.items():
    #         messages.error(request, value)
       
    #     return render(request, 'LoginAndRegistration.html',context)
    # else:
        flag=models.confermLogin(request.POST)
        
        if(flag):
           
            
            request.session['email']=request.POST['email']
            user=User.objects.get(email=request.session['email'])
            request.session['id']=user.id
            
           
            context={
                'user':User.objects.get(id=request.session['id'])
            }
            return redirect('/mainPage')
        else:
            return redirect('/')
def addNewAnimal(request):
    
    user=User.objects.get(id=1)
    category1 = Category.objects.get(id=request.POST['catgs'])
    Animal.objects.create(animal_name=request.POST['pet_name'],description=request.POST['pet_description'],price=request.POST['pet_price'],
    age=request.POST['pet_age'],isDelete=False,isAccepted=False,added_by=user, category=category1)
    return redirect('/mainPage')