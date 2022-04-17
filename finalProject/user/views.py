from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

from user import models
from user.models import User,Category,Animal

# Create your views here.
def index(request):
    return render(request,'login.html')

def openregisterpage(request):
    return render(request,'registration.html')

def openMainPage(request):
    context={
        'user': User.objects.get(id=request.session['id']),
        'admin': User.objects.get(rule_type=1),
        'lastcategories':models.getLastCategories(),
        'lastAnimals':models.getlastAnimals(),
    }
    return render (request, 'mainPage.html',context)

def showAllAnimals(request):
    context={
        'user': User.objects.get(id=request.session['id']),
        'allanimals':models.allAnimals(),
        'admin': User.objects.get(rule_type=1),

    }
    return render (request, 'all_animals.html',context)

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
    context = {
        'categories': Category.objects.all(),
        'user': User.objects.get(id=request.session['id']),
        'admin': User.objects.get(rule_type=1),
    }
    return render (request, 'all_catogries.html',context)

def aboutUs(request):
    context={
        'admin': User.objects.get(rule_type=1),
        'user': User.objects.get(id=request.session['id']),


    }
    return render (request, 'aboutUs.html')

def rigister(request):
    errors = User.objects.registration_validator(request.POST)
        
    if len(errors) > 0:
        
       
        for key, value in errors.items():
            messages.error(request, value)
        
        return render(request, 'registration.html')
    else:
        models.rigister(request.POST)
        return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
        
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        
        return render(request, 'registration.html')
    else:
        
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

def catogoryview(request, catogory_id):
    catogory = Category.objects.get(id=catogory_id)
    context = {
        'categories': Category.objects.filter(id=catogory_id),
        'animal_in_categories': Animal.objects.filter(category=catogory).filter(isDelete=False),
        'animals' : Animal.objects.all()
    }
    return render(request, 'all_animal_catg.html', context)

def showAnimalInfo(request,animalid):
    animal=models.getAnimal(animalid)
    context={
        'this_animal':animal,
        'current_user':User.objects.get(id=request.session['id']),
        'admin': User.objects.get(rule_type=1),
        'user': User.objects.get(id=request.session['id']),

    }
    return render(request,'animalinfo.html',context)

def editinfo(request,animal_id):
    context = {
    'animal':Animal.objects.get(id=animal_id)
    }
    return render(request,'editAnimal.html',context)
    
def search_status(request):
    print("hellllllllllllllllllllllllllllo")
    if request.method == "GET":
        search_text = request.GET['search_text']
        print("kkkkkkkkkkkkkkkkkkkk")
        if search_text is not None and search_text != u"":
            search_text = request.GET['search_text']
            statuss = Animal.objects.filter(animal_name = search_text)
            count= Animal.objects.filter(animal_name = search_text).count()
            print("ggggggggggggggggggggggggg")
            print(statuss)
        else:
            statuss = []
            count=0
            print("nnnnnoooooo")

        return render(request, 'mainPage.html', {'statuss':statuss,'count':count, 'user': User.objects.get(id=request.session['id']),
        'admin': User.objects.get(rule_type=1),
        'lastcategories':models.getLastCategories(),
        'lastAnimals':models.getlastAnimals(),})
