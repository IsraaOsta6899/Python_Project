from django.urls import path,include
from Adminn import views

urlpatterns = [
    path('adminn', views.index),
    
]