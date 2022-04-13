from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'login.html')
def openregisterpage(request):
    return render(request,'registration.html')
def openMainPage(request):
    return render (request, 'mainPage.html')
