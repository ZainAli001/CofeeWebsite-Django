from django.shortcuts import render

# Create your views here.
def home(request,*args,**kawrgs):
    return render(request,'home.html')

