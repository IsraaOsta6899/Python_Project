from django.db import models

class Rule(models.Model):
    rule_name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=10)
    city=models.CharField(max_length=45)
    gender=models.CharField(max_length=10,default="")
    rule_type=models.ForeignKey(Rule,related_name='users_in_this_rule', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

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
    added_by=models.ForeignKey(User,related_name='added_animals', on_delete=models.CASCADE)
    category=models.ForeignKey(Category,related_name='animals_in_this_category', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)