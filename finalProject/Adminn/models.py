from django.db import models

from user.models import Animal
def getAllRequests(info):
    print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    return Animal.objects.filter(isAccepted=0).filter(isDelete=0)

def accept(info , id ):
    animal = Animal.objects.get(id=id)
    animal.isAccepted=True
    animal.save()
    return

def reject(info , id ):
    animal = Animal.objects.get(id=id)
    animal.isDelete=True
    animal.save()
    return
def edit_info1(info,animal1_id):
    this_animal=Animal.objects.get(id=animal1_id)
    this_animal.animal_name=info['pet_name']
    this_animal.price=info['pet_price']
    this_animal.age=info['pet_age']
    
    this_animal.save()
    return
def deleteAnimal(id):
    animal = Animal.objects.get(id=id)
    animal.isDelete=True
    animal.save()
    return

