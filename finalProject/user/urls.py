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

]