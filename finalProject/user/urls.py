from django.urls import path,include
from user import views

urlpatterns = [
    path('', views.index),
    path('registerForm', views.openregisterpage)
    
]