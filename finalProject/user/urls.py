from django.urls import path,include
from user import views

urlpatterns = [
    path('', views.index),
    path('registerForm', views.openregisterpage),
    path('mainPage',  views.openMainPage),
    path('showAllAnimals',  views.showAllAnimals),
    path('addAnimalPage',  views.addAnimalPage),
    path('allCategories',  views.allCategories),
    path('aboutUs',  views.aboutUs),
    path('rigister', views.rigister),
    path('login',views.login),
    path('addNewAnimal', views.addNewAnimal),
    path('catogries/<int:catogory_id>', views.catogoryview),
]