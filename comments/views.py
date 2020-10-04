from django.shortcuts import render, redirect
from .models import Comment
# Create your views here.

def createComment(request):
    print(request)
    # if request.method
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    return render(request, 'home.html')

