import bcrypt
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import UserManager

import re

class Rule(models.Model):
    DEFAULT_PK=1
    rule_name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id
# def get_foo():
#     return Rule.objects.get(id=1)
class CUserManager(models.Manager):
        def registration_validator(self, postData):
            errors = {}
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            phone_regex=r'^\?1?\d{10}$'
            
            if len(postData['fname'])<2 :
                errors["fname"] = " first name must be more than 1 letters"

            if len(postData['lname']) < 2:
                errors["lname"] =  " first name must be more than 1 letters"
            
            if not EMAIL_REGEX.match(postData['email']):      
                errors['email'] = "Invalid email address!"

            if re.search('[A-Z]', postData['password'])==None and re.search('[0-9]', postData['password'])==None and re.search('[^A-Za-z0-9]', postData['password'])==None and len(postData['password'])<8:         
                errors["password"] = "password should contains capital letters and numbers and small letters and more than 8 letters"
           
            if postData['password']  != postData['cpassword']:
                errors['repassword'] = "password didn't matches!!"
            
            if len(postData['cpassword']) < 1:
                errors["cpassword"] = "confirm password is requierd"   

            if len(postData['city'])<1:
                errors["city"] = " city is required field"

            if len(postData['phone'])<10 and re.search('[A-Z]', postData['phone'])!= None  :   
                errors['phone'] = "Invalid phone number!"
            return errors
        def login_validator(self, postData):
            errors1 = {}
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            phone_regex=r'^\?1?\d{10}$'
            
            
            
            if not EMAIL_REGEX.match(postData['email']):      
                errors1['email'] = "Invalid email address!"

            if  len(postData['password'])<1:         
                errors1["password"] = "both field are requierd"
            if  len(postData['email'])<1:         
                errors1["email"] = "both field are requierd"
           
            
            return errors1
        def adding_validator(self, postData):
            errors2 = {}
            if len(postData['pet_name']) < 2:
                errors2["pet_name"] = "animal name should be at least 2 characters"
            if len(postData['pet_age']) < 1:
                errors2["pet_age"] = "animal age should be a number"
            try:
                val=int(postData['pet_age'])
            except ValueError:
                errors2["pet_age1"] = "animal age should be a number"
            if len(postData['pet_price']) < 1:
                errors2["pet_price"] = "animal age should be a number"
            try:
                val=int(postData['pet_price'])
            except ValueError:
                errors2["petprice1"] = "animal age should be a number"

            return errors2


class User(AbstractBaseUser, PermissionsMixin):
    
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=10)
    city=models.CharField(max_length=45)
    gender=models.CharField(max_length=10,default="")
    rule_type=models.ForeignKey(Rule,related_name='users_in_this_rule', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(_('staff status'),default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects =CUserManager() 
    # objects = UserManager()
    

    def __str__(self):
        return self.email

class Category(models.Model):
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Animal(models.Model):
    animal_name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()
    age=models.FloatField()
    image=models.ImageField(upload_to='Media', blank=True)

    isDelete=models.BooleanField()
    isAccepted=models.BooleanField()
    added_by=models.ForeignKey(User,related_name='added_animals', on_delete=models.CASCADE)
    category=models.ForeignKey(Category,related_name='animals_in_this_category', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CUserManager()
   

def rigister(info):
    all_Users=User.objects.all().count
    if all_Users==0:
        b=Rule.objects.get(id=1)
        password=info['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=info['fname'],last_name=info['lname'],email=info['email'], password=pw_hash,phone_number=info['phone'],rule_type=b)
    
    else:
        a=Rule.objects.get(id=2)
        password=info['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=info['fname'],last_name=info['lname'],email=info['email'], password=pw_hash,phone_number=info['phone'],rule_type=a)
    return
def confermLogin(info):
    user = User.objects.filter(email=info['email'])
    print("jjjjjjjjjjjjjjjjjjjjjjjj")
    print(len(user))
    if(len(user)!=0):
        if user[0]:
            if bcrypt.checkpw(info['password'].encode(), user[0].password.encode()):
                return True
            else:
                return False
        else: 
            return False
    else:
        return False
def getLastCategories():
    last_four = Category.objects.all().order_by('-id')[:4]
    return last_four
def getlastAnimals():
    countOfAllAcceptedAnimals=Animal.objects.all().filter(isAccepted=True).filter(isDelete=False).count()
    if countOfAllAcceptedAnimals >= 4:
        allAcceptedAnimals=Animal.objects.all().filter(isAccepted=True).filter(isDelete=False).order_by('-id')[:4]
    elif countOfAllAcceptedAnimals==3:
        allAcceptedAnimals=Animal.objects.all().filter(isAccepted=True).filter(isDelete=False).order_by('-id')[:3]
    elif countOfAllAcceptedAnimals==2:
        allAcceptedAnimals=Animal.objects.all().filter(isAccepted=True).filter(isDelete=False).order_by('-id')[:2]
    elif countOfAllAcceptedAnimals==1:
        allAcceptedAnimals=Animal.objects.all().filter(isAccepted=True).filter(isDelete=False).order_by('-id')[:1]
    elif countOfAllAcceptedAnimals==0:
        allAcceptedAnimals=Animal.objects.all().filter(isAccepted=True).filter(isDelete=False).order_by('-id')[:0]


    return allAcceptedAnimals
def allAnimals():
    return Animal.objects.filter(isAccepted=True ).filter(isDelete=False)

def getAnimal(animalid):
    return Animal.objects.get(id=animalid)
def addnewcategory1(info):
    c=Category.objects.create(name=info['cat_name'])
    return

# c=Rule.objects.get(id=1)
# password="12345678"
# pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# u=User.objects.create(first_name="ahmad",rule_type=c, last_name="usta", city="nablus",phone_number="0569227507",gender="male",email="ahmad@hotmail.com",password= pw_hash)