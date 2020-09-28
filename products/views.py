from django.shortcuts import render

# Create your views here.

def getHome(request):
    return render(request, 'products/home.html')