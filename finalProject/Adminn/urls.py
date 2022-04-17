from django.urls import path,include
from Adminn import views

urlpatterns = [
    path('adminn', views.index),
    path('requestPage', views.requestPage),
    path('accept/<int:animalid>',views.accept ),
    path('reject/<int:animalid>',views.reject ),
    path('edit_this_animal/<int:animal1_id>',views.edit_info),
    path('deleteAnimal/<int:animalid>', views.deleteAnimal)

    
]