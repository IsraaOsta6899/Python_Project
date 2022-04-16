import bcrypt
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Rule(models.Model):
    DEFAULT_PK=1
    rule_name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id
# def get_foo():
#     return Rule.objects.get(id=1)
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

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Category(models.Model):
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Animal(models.Model):
    animal_name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()
    age=models.FloatField()
    image=models.ImageField()
    isDelete=models.BooleanField()
    isAccepted=models.BooleanField()
    added_by=models.ForeignKey(User,related_name='added_animals', on_delete=models.CASCADE)
    category=models.ForeignKey(Category,related_name='animals_in_this_category', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   

def rigister(info):
    a=Rule.objects.get(id=2)
    User.objects.create(first_name=info['fname'],last_name=info['lname'],email=info['email'], password=info['password'],phone_number=info['phone'],rule_type=a)
    return
def confermLogin(info):
    user = User.objects.get(email=info['email'])

    if user:
        if crypt.checkpw(info['password'].encode(), user.password.encode()):
             return True
        else:
            return False
    else: 
        return False
