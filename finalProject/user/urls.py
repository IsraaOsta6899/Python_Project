from django.urls import path,include
from user import views
from django.conf import settings
from django.conf.urls.static import static
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
    path('showAnimalInfo/<int:animalid>', views.showAnimalInfo),
    path('edit_info/<int:animal_id>',views.editinfo),
    path('status/search_status/',views.search_status),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
